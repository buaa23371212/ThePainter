import argparse
from .circle_parser import add_circle_arguments
from .square_parser import add_square_arguments

def parse_arguments():
    """解析命令行参数并返回结果"""
    parser = argparse.ArgumentParser(description='在画图工具中绘制图形')
    
    # 添加绘图命令
    subparsers = parser.add_subparsers(dest='command', help='绘图命令')
    
    # 添加圆形命令解析
    add_circle_arguments(subparsers)

    # 添加正方形命令解析
    add_square_arguments(subparsers)
    
    return parser.parse_args()