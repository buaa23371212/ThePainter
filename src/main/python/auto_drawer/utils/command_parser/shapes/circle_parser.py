def add_circle_arguments(subparsers):
    """为圆形命令添加参数解析"""
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

    # TODO: 相对坐标
    
    return circle_parser