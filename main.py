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
from utils.tools.tools import open_paint
from utils.tools.layer_tools import select_layer, add_layer, select_layer_operation
from parser.command_parser import parse_arguments

# ==============================
# 绘图命令模块导入区
# ==============================
from drawer.circle_drawer import select_circle_tool, draw_circle_command
from drawer.ellipse_drawer import select_ellipse_tool, draw_ellipse_command
from drawer.square_drawer import select_square_tool, draw_square_command
from drawer.rectangle_drawer import select_rectangle_tool, draw_rectangle_command
from drawer.polygon_drawer import select_polygon_tool, draw_polygon_command
from drawer.line_drawer import select_line_tool, draw_line_command
from drawer.rounded_rectangle_drawer import select_rounded_rectangle_tool, draw_rounded_rectangle_command

# ==============================
# 颜色填充模块导入区
# ==============================
from colorer.colorer import choose_color

# ==============================
# 日志记录模块导入区
# ==============================
from terminal_logger.logger import info, warn, error
from terminal_logger.command_logger import title, step

# ==============================
# 全局状态变量
# ==============================
current_color = None  # 当前已选择的颜色
current_tool = None   # 当前已选择的绘图工具

# ==============================
# 批处理辅助函数模块
# ==============================
def extract_comment_words(line: str) -> str:
    """
    提取命令文件中的注释内容
    
    功能:
    - 解析以'#'开头的注释行
    - 移除注释符号及前导空白符
    
    :param line: 输入行文本
    :return: 纯注释内容字符串（非注释行返回空字符串）
    """
    if line.startswith("# "):
        return line.lstrip()[1:].lstrip()
    return ""


# ==============================
# 命令分发核心模块
# ==============================
def _dispatch_command(args):
    """
    命令分发主控制器
    
    功能:
    - 根据命令类型路由到对应的处理模块
    - 支持图形绘制、鼠标控制和图层操作三类命令
    
    :param args: 解析后的命令行参数对象
    """
    # 图形绘制命令路由
    if args.command in ['circle', 'ellipse', 'square', 'rectangle', 
                       'rounded_rectangle', 'polygon', 'line']:
        _dispatch_shape_command(args)
    
    # 鼠标控制命令路由
    elif args.command in ['move_mouse', 'mouse_click', 'right_click']:
        _dispatch_mouse_command(args)
    
    # 图层操作命令路由
    elif args.command in ['add_layer', 'choose_layer', 'layer_operation']:
        _dispatch_layer_command(args)
    
    # 未知命令处理
    else:
        warn(True, f"暂不支持的命令: {args.command}", True)


def _dispatch_shape_command(args):
    """
    图形绘制命令分发器
    
    功能:
    - 根据图形类型选择对应工具
    - 执行图形绘制操作
    
    :param args: 包含图形参数的命令行参数对象
    """
    shape_commands = {
        'circle': (select_circle_tool, draw_circle_command),
        'ellipse': (select_ellipse_tool, draw_ellipse_command),
        'square': (select_square_tool, draw_square_command),
        'rectangle': (select_rectangle_tool, draw_rectangle_command),
        'rounded_rectangle': (select_rounded_rectangle_tool, draw_rounded_rectangle_command),
        'polygon': (select_polygon_tool, draw_polygon_command),
        'line': (select_line_tool, draw_line_command)
    }
    
    if args.command in shape_commands:
        select_tool, draw_command = shape_commands[args.command]
        select_tool()
        draw_command(args)


def _dispatch_mouse_command(args):
    """
    鼠标控制命令分发器
    
    功能:
    - 执行鼠标移动、左键点击和右键点击操作
    
    :param args: 包含坐标参数的命令行参数对象
    """
    if args.command == 'move_mouse':
        info(False, f"将鼠标移动到位置 ({args.x}, {args.y})", True)
        pyautogui.moveTo(args.x, args.y)
    elif args.command == 'mouse_click':
        info(False, f"在位置 ({args.x}, {args.y}) 模拟鼠标点击", True)
        pyautogui.click(x=args.x, y=args.y)
    elif args.command == 'right_click':
        info(False, f"在位置 ({args.x}, {args.y}) 模拟鼠标右键点击", True)
        pyautogui.rightClick(x=args.x, y=args.y)


def _dispatch_layer_command(args):
    """
    图层操作命令分发器
    
    功能:
    - 执行图层添加、选择和操作命令
    
    :param args: 包含图层参数的命令行参数对象
    """
    if args.command == 'add_layer':
        info(False, "添加新图层", True)
        add_layer()
    elif args.command == 'choose_layer':
        info(False, f"选择图层 ID: {args.layer_id}", True)
        select_layer(args.layer_id)
    elif args.command == 'layer_operation':
        info(False, f"对图层 ID: {args.layer_id} 执行操作: {args.operation}", True)
        select_layer_operation(args.operation, args.layer_id)
    else:
        warn(True, f"暂不支持的图层命令: {args.command}", True)


# ==============================
# 命令执行模块
# ==============================
def execute_command(args):
    """
    命令执行入口
    
    功能:
    - 执行单条绘图命令
    - 提供异常捕获和处理
    
    :param args: 解析后的命令行参数对象
    """
    global current_color, current_tool

    try:
        if args.color:
            info(True, f"选择颜色: {args.color}", True)
            choose_color(args.color)

        _dispatch_command(args)
    except Exception as e:
        error(True, f"操作失败: {str(e)}", True)


# ==============================
# 批处理模块
# ==============================
def _process_batch_commands(input_file_path):
    """
    批量命令处理器
    
    功能:
    - 解析并执行命令文件中的指令序列
    - 支持标题、步骤说明和命令混合格式
    
    文件格式说明:
    # ====================
    # 标题文本
    # ====================
    # 1. 步骤说明
    command arg1 arg2
    
    :param input_file_path: 命令文件路径
    """
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # 跳过空行
            if not line:
                i += 1
                continue

            # 标题块处理 (三行格式)
            if line.startswith("# =") and i + 2 < len(lines):
                title_line = lines[i + 1].strip()
                title(True, extract_comment_words(title_line), True)
                i += 3  # 跳过标题块的三行
                continue

            # 步骤说明处理
            if line.startswith("# ") and "." in line:
                step(True, extract_comment_words(line), True)
                i += 1
                continue
            
            # 命令执行
            if not line.startswith("#"):
                command_args = line.split()
                parsed_args = parse_arguments(command_args)
                execute_command(parsed_args)
                i += 1


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
            _process_batch_commands(args.input_file)  # 执行批量命令
            info(True, "画图工具保持打开状态", True)
        except Exception as e:
            error(True, f"批量操作失败: {str(e)}", True)
    else:
        # 单命令模式
        try:
            open_paint()  # 打开画图工具
            execute_command(args)  # 执行单条命令
            info(True, "画图工具保持打开状态", True)
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