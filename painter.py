"""
绘图自动化工具主程序

功能概述：
1. 支持单命令执行和批量命令文件处理
2. 实现图形绘制、图层操作和鼠标控制三大功能
3. 提供详细的执行日志和错误处理
"""

import os
import pyautogui

# ==============================
# 工具模块导入区
# ==============================
from painter_tools.painter_tools.general_tools import open_paint, minimize_paint
from command_handler.command_parser import parse_arguments
from command_handler.command_executor import execute_command, process_batch_commands

# ==============================
# 日志记录模块导入区
# ==============================
from painter_tools.terminal_logger.logger import info, error

# ==============================
# 主程序模块
# ==============================
def main():
    """
    程序主控制器
    
    执行流程:
    1. 解析命令行参数
    2. 打开画图工具
    3. 根据输入类型执行命令:
       - 输入文件: 执行批量命令
       - 单命令: 执行单个绘图命令
    4. 异常处理和状态报告
    """
    # 步骤1: 解析命令行参数
    args = parse_arguments()

    if args.input_file:
        # 批量命令模式
        try:
            open_paint()  # 打开画图工具
            process_batch_commands(args.input_file)  # 执行批量命令
            info(True, "画图工具保持打开状态", True)
            # minimize_paint()
        except Exception as e:
            error(True, f"批量操作失败: {str(e)}", True)
    else:
        # 单命令模式
        try:
            open_paint()  # 打开画图工具
            execute_command(args)  # 执行单条命令
            info(True, "画图工具保持打开状态", True)
            minimize_paint()
        except Exception as e:
            error(True, f"命令执行失败: {str(e)}", True)


# ==============================
# 程序入口点
# ==============================
if __name__ == "__main__":
    """
    程序入口
    
    系统要求:
    - 仅支持Windows操作系统
    
    执行流程:
    1. 检测操作系统类型
    2. Windows系统: 执行主程序
    3. 非Windows系统: 显示错误并退出
    """
    if os.name == 'nt':  # Windows系统
        info(True, "检测到Windows系统，开始执行绘制任务...", True)
        main()
        info(True, "脚本执行完毕", True)
    else:  # 非Windows系统
        error(True, "此脚本仅支持Windows系统", True)