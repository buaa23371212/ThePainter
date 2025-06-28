def add_rectangle_arguments(subparsers):
    """为矩形命令添加参数解析"""
    rectangle_parser = subparsers.add_parser('rectangle', help='绘制矩形')
    rectangle_group = rectangle_parser.add_mutually_exclusive_group()
    
    rectangle_group.add_argument(
        '-bounding', 
        nargs=4, 
        type=int, 
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        help='通过起点和终点绘制矩形（四个整数坐标）'
    )
    rectangle_group.add_argument(
        '-center', 
        nargs=4, 
        type=int, 
        metavar=('center_x', 'center_y', 'width', 'height'),
        help='通过中心点和长宽绘制矩形'
    )
    
    return rectangle_parser