import argparse

def parse_arguments():
    """解析命令行参数并返回结果"""
    parser = argparse.ArgumentParser(description='在画图工具中绘制图形')
    
    # 添加绘图命令
    subparsers = parser.add_subparsers(dest='command', help='绘图命令')
    
    # 圆形命令
    circle_parser = subparsers.add_parser('circle', help='绘制圆形')
    circle_group = circle_parser.add_mutually_exclusive_group()
    
    circle_group.add_argument(
        '-bounding', 
        nargs=4, 
        type=int, 
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        help='通过起点和终点绘制圆形（四个整数坐标）'
    )
    circle_group.add_argument(
        '-center', 
        nargs=3, 
        type=int, 
        metavar=('center_x', 'center_y', 'radius'),
        help='通过圆心和半径绘制圆形'
    )
    
    # 这里可以添加其他图形的参数解析
    # 例如：
    # house_parser = subparsers.add_parser('house', help='绘制房子')
    # house_parser.add_argument(...)
    
    return parser.parse_args()