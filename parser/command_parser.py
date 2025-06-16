import argparse
from .circle_parser import add_circle_arguments
from .square_parser import add_square_arguments

def parse_arguments(args=None):
    """解析命令行参数并返回结果"""
    parser = argparse.ArgumentParser(description='在画图工具中绘制图形')

    # 添加输入文件参数
    parser.add_argument('-input_file', type=str, help='包含多个绘图命令的输入文件')

    # 添加绘图命令
    subparsers = parser.add_subparsers(dest='command', help='绘图命令')

    # 添加圆形命令解析
    add_circle_arguments(subparsers)

    # 添加正方形命令解析
    add_square_arguments(subparsers)

    return parser.parse_args(args)