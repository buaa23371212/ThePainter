import os
import subprocess

from ui.foo.utils.terminal_logger.logger import info, error

from ui.foo.configs import ui_config


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
    
    project_root = ui_config.painter_dir
    
    # 构建命令
    command = f"python painter.py -input_file \"{file_path}\""
    
    # 记录执行信息
    info(True, f"执行命令: {command}", True)
    text_view.append("\n\n=== 命令执行开始 ===")
    text_view.append(f"执行文件: {os.path.basename(file_path)}")
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