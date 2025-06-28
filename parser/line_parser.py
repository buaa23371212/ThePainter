def add_line_arguments(subparsers):
    """为直线命令添加参数解析
    
    支持两种方式绘制直线：
    1. 起点+终点坐标
    2. 起点+方向向量
    """
    line_parser = subparsers.add_parser('line', help='绘制直线')
    line_group = line_parser.add_mutually_exclusive_group(required=True)
    
    # 起点+终点方式
    line_group.add_argument(
        '-points', 
        nargs=4, 
        type=int, 
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        dest='points',
        help='通过起点和终点坐标绘制直线'
    )
    
    # 起点+方向向量方式
    line_group.add_argument(
        '-vector', 
        nargs=4, 
        type=int, 
        metavar=('start_x', 'start_y', 'dx', 'dy'),
        dest='vector',
        help='通过起点和方向向量绘制直线 (dx, dy)'
    )
    
    return line_parser