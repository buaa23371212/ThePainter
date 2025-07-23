import os
import subprocess
import threading

from src.main.python.terminal_logger.logger import info, error, debug

from src.main.python.configs import project_config

def record_execution_info(project_root, command, text_view, other_msg):
    """记录执行信息"""
    info(True, f"执行命令: {command}", True)
    text_view.append("\n\n=== 命令执行开始 ===")
    text_view.append(other_msg)
    text_view.append(f"执行命令: {command}")

    try:
        # 执行命令
        process = subprocess.Popen(
            command,
            cwd=project_root,  # 设置工作目录为项目根目录
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            encoding='utf-8'
        )

        # 读取输出并实时显示
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                text_view.append(output.strip())

        # 检查退出码
        return_code = process.poll()
        if return_code == 0:
            text_view.append("状态: 执行成功")
        else:
            # 读取错误输出
            error_output = process.stderr.read()
            text_view.append(f"状态: 执行失败 (退出码: {return_code})")
            text_view.append("错误信息:")
            text_view.append(error_output)

        text_view.append("=== 命令执行结束 ===")
        return return_code == 0

    except Exception as e:
        text_view.append(f"执行命令时出错: {str(e)}")
        error(True, f"执行命令时出错: {str(e)}", True)
        text_view.append("=== 命令执行结束（异常） ===")
        return False

def execute_command_file(file_path, text_view):
    """
    执行命令文件并将输出实时显示在文本视图中
    
    参数:
        file_path: 命令文件路径
        text_view: QTextEdit 对象，用于显示输出
    """
    if not file_path or not os.path.isfile(file_path):
        error(True, "没有可执行的命令文件", True)
        text_view.append("错误: 没有可执行的命令文件")
        return False
    
    project_root = project_config.painter_dir
    
    # 构建命令
    command = f"python painter.py -input_file \"{file_path}\""
    
    # 记录执行信息
    return record_execution_info(project_root, command, text_view, f"执行文件: {os.path.basename(file_path)}")

def execute_listening_command(text_view, action="record", input_file=None, output_file=None, print_commands=False):
    """
    执行监听器命令

    参数:
        text_view: QTextEdit 对象，用于显示输出
        action: 操作类型，可选值: 'record', 'export', 'convert', 'full', 'parse', 'parse_and_save'
        input_file: 输入文件路径（用于parse和parse_and_save操作）
        output_file: 输出文件路径（用于export和parse_and_save操作）
        print_commands: 是否打印命令（用于convert和parse操作）
    """
    project_root = project_config.listener_dir
    command = f"python listener.py -a {action}"

    # 添加输入文件参数
    if input_file and action in ['parse', 'parse_and_save']:
        command += f" -f \"{input_file}\""

    # 添加输出文件参数
    if output_file and action in ['export', 'parse_and_save']:
        command += f" -c \"{output_file}\""

    # 添加打印命令参数
    if print_commands and action in ['convert', 'parse']:
        command += " -p"

    def run_command():
        record_execution_info(project_root, command, text_view, f"执行监听器操作: {action}")

    # 启动线程执行命令，避免阻塞UI
    threading.Thread(target=run_command, daemon=True).start()
    return True  # 立即返回，不等待命令执行完成