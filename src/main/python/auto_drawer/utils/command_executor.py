import re
import time
import pyautogui

# ==============================
# 工具模块导入区
# ==============================
from src.main.python.configs.screen_config import CANVAS_BLANK_POSITION
from src.main.python.utils.auto_speed_manager import auto_speed_config
from .command_parser.command_parser import parse_arguments
from .command_parser.control import SUPPORTED_MOUSE_OPERATIONS
from .command_parser.tools import SUPPORTED_LAYER_OPERATION
from .layer_tools import select_layer, add_layer, select_layer_operation

# ==============================
# 绘图命令模块导入区
# ==============================
from .command_parser.shapes import SUPPORTED_SHAPES
from .drawer import SHAPE_COMMANDS

# ==============================
# 颜色填充模块导入区
# ==============================
from .colorer import select_fill_tool, choose_color, fill_color

# ==============================
# 文本输入模块导入区
# ==============================
from .texter import select_texter_tool, create_text

# ==============================
# 日志记录模块导入区
# ==============================
from src.main.python.terminal_logger.logger import info, warn, error
from src.main.python.terminal_logger.command_logger import title, step

# ==============================
# 全局状态变量
# ==============================
current_tool = "pen"                    # 当前已选择的绘图工具
current_color = "black"                 # 当前已选择的颜色
current_shape = None                    # 当前已选择的图形工具
# TODO
current_shape_border = "solid"
current_shape_fill = "solid"
current_shape_thickness = 5
current_font = "Microsoft YaHei UI"
current_font_size = 11
current_pen = "brush"
current_layer = 1                       # 当前已选择的图层

# ==============================
# 批处理辅助函数模块
# ==============================
def _extract_comment_words(line: str) -> str:
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
    global current_color
    
    if args.command is None:
        if args.color is not None and args.color != current_color:
            info(False, f"设置当前颜色: {args.color}", True)
            current_color = args.color
            choose_color(args.color)
        
        return
    
    # 图形绘制命令路由
    if args.command in SUPPORTED_SHAPES:
        info(False, f"绘制图形: {args.command}", True)
        _dispatch_shape_command(args)

    # 填充颜色命令路由
    elif args.command == 'fill':
        info(False, f"填充颜色: {args.color} 到位置 ({args.x}, {args.y})", True)
        _dispatch_fill_command(args)

    # 文本输入命令路由
    elif args.command == 'text':
        info(False, f"输入文本: {args.text} 到位置 ({args.x}, {args.y})", True)
        _dispatch_text_command(args)
    
    # 鼠标控制命令路由
    elif args.command in SUPPORTED_MOUSE_OPERATIONS:
        _dispatch_mouse_command(args)
    
    # 图层操作命令路由
    elif args.command in SUPPORTED_LAYER_OPERATION:
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
    global current_shape, current_tool, current_color

    shape_commands = SHAPE_COMMANDS

    # Step 1: 选工具
    if args.command in shape_commands:
        select_tool, draw_command = shape_commands[args.command]

        if current_shape != args.command or current_tool != 'shape':
            current_shape = args.command
            current_tool = 'shape'
            select_tool()

        # Step 2: 选择颜色
        if args.color is not None and args.color != current_color:
            info(False, f"选择颜色: {args.color}", True)
            current_color = args.color
            choose_color(args.color)

        # Step 3: 执行绘制命令
        draw_command(args)
    
    else:
        warn(True, f"未知图形命令: {args.command}", True)
        return


def _dispatch_fill_command(args):
    """
    填充命令分发器
    
    功能:
    - 执行颜色填充操作
    
    :param args: 包含填充参数的命令行参数对象
    """
    global current_color, current_tool

    if current_tool != 'fill':
        current_tool = 'fill'
        select_fill_tool()

    if args.color != current_color:
        current_color = args.color
        choose_color(args.color)

    fill_color(args.color, args.x, args.y)

def _dispatch_text_command(args):
    """
    文本输入命令分发器
    
    功能:
    - 执行文本输入操作
    
    :param args: 包含文本参数的命令行参数对象
    """
    global current_tool

    if current_tool != 'text':
        current_tool = 'text'
        select_texter_tool()

    info(False, f"在位置 ({args.x}, {args.y}) 输入文本: {args.text}", True)
    create_text(args.text, args.x, args.y)

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
        time.sleep(2)
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
        pass    # TODO
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
    try:
        _dispatch_command(args)
        
        # 取消上一个图案选中
        pyautogui.moveTo(CANVAS_BLANK_POSITION[0], CANVAS_BLANK_POSITION[1], auto_speed_config.ACTUAL_MOUSE_MOVE_SPEED)  # 确保鼠标在画布空白处
        pyautogui.click()                                   # 激活画布窗口
        time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)     # 等待点击生效
    except Exception as e:
        error(True, f"操作失败: {str(e)}", True)


# ==============================
# 批处理模块
# ==============================
def process_batch_commands(input_file_path, flags={}):
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
    # TODO: jump to step 27
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if flags.get('stop', False):  # 使用get方法安全访问
                info(True, "用户通过热键中断批量命令执行", True)
                break

            line = lines[i].strip()

            # 跳过空行
            if not line:
                i += 1
                continue

            # 标题块处理 (三行格式)
            if line.startswith("# =") and i + 2 < len(lines):
                title_line = lines[i + 1].strip()
                end_line = lines[i + 2].strip()
                if end_line.startswith("# ="):
                    title(True, _extract_comment_words(title_line))
                    i += 3  # 跳过标题块的三行
                    continue
                else:
                    i += 1
                    continue

            # 步骤说明处理
            if line.startswith("# "):
                comment = _extract_comment_words(line)
                # 用正则判断是否以“数字+点+空格”开头，支持多位数字
                if comment and re.match(r"^\d+\.\s", comment):
                    step(True, comment)
                elif comment:
                    step(False, comment)
                i += 1
                continue
            
            # 命令执行
            if not line.startswith("#"):
                # 去除行内注释
                command_line = line.split("#")[0].strip()
                info(False, f"执行命令: {command_line}", True)
                if not command_line:
                    i += 1
                    continue
                command_args = command_line.split()
                parsed_args = parse_arguments(command_args)
                execute_command(parsed_args)
                
            i += 1