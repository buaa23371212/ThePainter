import pyautogui

# ==============================
# 工具模块导入区
# ==============================
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
from colorer.colorer import select_fill_tool, choose_color, fill_color

# ==============================
# 日志记录模块导入区
# ==============================
from terminal_logger.logger import info, warn, error, debug
from terminal_logger.command_logger import title, step

# ==============================
# 全局状态变量
# ==============================
current_color = "black"     # 当前已选择的颜色
current_tool = "brush"      # 当前已选择的绘图工具
current_shape = None        # 当前已选择的图形工具
current_layer = 1           # 当前已选择的图层

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
    if args.command is None:
        pass
    
    # 图形绘制命令路由
    elif args.command in ['circle', 'ellipse', 'square', 'rectangle', 
                       'rounded_rectangle', 'polygon', 'line']:
        info(False, f"绘制图形: {args.command}", True)
        _dispatch_shape_command(args)

    # 填充颜色命令路由
    elif args.command == 'fill':
        info(False, f"填充颜色: {args.color} 到位置 ({args.x}, {args.y})", True)
        _dispatch_fill_command(args)
    
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
    global current_shape, current_tool, current_color

    shape_commands = {
        'circle': (select_circle_tool, draw_circle_command),
        'ellipse': (select_ellipse_tool, draw_ellipse_command),
        'square': (select_square_tool, draw_square_command),
        'rectangle': (select_rectangle_tool, draw_rectangle_command),
        'rounded_rectangle': (select_rounded_rectangle_tool, draw_rounded_rectangle_command),
        'polygon': (select_polygon_tool, draw_polygon_command),
        'line': (select_line_tool, draw_line_command)
    }

    # Step 1: 选工具
    if current_tool != 'shape':
        current_tool = 'shape'
    
    if args.command in shape_commands:
        select_tool, draw_command = shape_commands[args.command]

        if current_shape != args.command:
            current_shape = args.command
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
    global current_color

    try:
        _dispatch_command(args)
    except Exception as e:
        error(True, f"操作失败: {str(e)}", True)


# ==============================
# 批处理模块
# ==============================
def process_batch_commands(input_file_path):
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
                title(True, _extract_comment_words(title_line), True)
                i += 3  # 跳过标题块的三行
                continue

            # 步骤说明处理
            if line.startswith("# "):
                comment = _extract_comment_words(line)
                # 如果注释内容以数字加点开头，视为步骤，否则视为普通说明
                if comment and (comment[0].isdigit() and comment[1:3] == ". "):
                    step(True, comment)
                elif comment:
                    step(False, comment)
                i += 1
                continue
            
            # 命令执行
            if not line.startswith("#"):
                command_args = line.split()
                parsed_args = parse_arguments(command_args)
                execute_command(parsed_args)
                
            i += 1