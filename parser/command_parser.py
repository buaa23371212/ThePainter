import argparse
from .circle_parser import add_circle_arguments
from .ellipse_parser import add_ellipse_arguments
from .square_parser import add_square_arguments
from .rectangle_parser import add_rectangle_arguments
from .polygon_parser import add_polygon_arguments
from .line_parser import add_line_arguments
from .rounded_rectangle_parser import add_rounded_rectangle_arguments
from .mouse_parser import add_move_mouse_arguments, add_mouse_click_arguments, add_right_click_arguments

def parse_arguments(args=None):
    """解析命令行参数并返回结果"""
    parser = argparse.ArgumentParser(description='在画图工具中绘制图形')

    # 添加输入文件参数
    parser.add_argument('-input_file', type=str, help='包含多个绘图命令的输入文件')

    # 添加绘图命令
    subparsers = parser.add_subparsers(dest='command', help='绘图命令')

    # 添加各种图形命令解析
    add_ellipse_arguments(subparsers)
    add_rectangle_arguments(subparsers)
    add_line_arguments(subparsers)
    add_polygon_arguments(subparsers)
    add_rounded_rectangle_arguments(subparsers)
    add_circle_arguments(subparsers)
    add_square_arguments(subparsers)

    add_move_mouse_arguments(subparsers)
    add_mouse_click_arguments(subparsers)
    add_right_click_arguments(subparsers)

    return parser.parse_args(args)