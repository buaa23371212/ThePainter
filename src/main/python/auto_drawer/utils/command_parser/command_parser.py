import argparse

from .shapes.circle_parser import add_circle_arguments
from .shapes.ellipse_parser import add_ellipse_arguments
from .shapes.square_parser import add_square_arguments
from .shapes.rectangle_parser import add_rectangle_arguments
from .shapes.rounded_rectangle_parser import add_rounded_rectangle_arguments
from .shapes.polygon_parser import add_polygon_arguments
from .shapes.line_parser import add_line_arguments
from .shapes.polyline_parser import add_polyline_arguments
from .shapes.curve_parser import add_curve_arguments, add_multicurve_arguments

from .control.mouse_parser import add_move_mouse_arguments, add_mouse_click_arguments, add_right_click_arguments
from .control.png_saver import add_png_saver_arguments
from .control.page_closer import add_close_page_argument

from .tools.layer_parser import add_layer_choose_arguments, add_layer_operation_arguments, add_new_layer_arguments

from .tools.color_parser import add_color_parser
from .tools.color_parser import add_fill_arguments

from .tools.text_parser import add_text_arguments

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
    add_curve_arguments(subparsers)
    add_multicurve_arguments(subparsers)
    add_polyline_arguments(subparsers)

    # 添加颜色选择命令
    # 给 parser 添加一个可选参数
    add_color_parser(parser)
    add_fill_arguments(subparsers)

    # 添加鼠标控制命令
    add_move_mouse_arguments(subparsers)
    add_mouse_click_arguments(subparsers)
    add_right_click_arguments(subparsers)
    add_close_page_argument(subparsers)

    # 添加图层控制命令
    add_layer_choose_arguments(subparsers)
    add_layer_operation_arguments(subparsers)
    add_new_layer_arguments(subparsers)

    # 添加文本输入命令
    add_text_arguments(subparsers)

    # 添加图片保存命令
    add_png_saver_arguments(subparsers)

    return parser.parse_args(args)