def add_square_arguments(subparsers):
    """为正方形命令添加参数解析"""
    square_parser = subparsers.add_parser('square', help='绘制正方形')
    square_group = square_parser.add_mutually_exclusive_group()
    
    square_group.add_argument(
        '-bounding', 
        nargs=4, 
        type=int, 
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        help='通过起点和终点绘制正方形（四个整数坐标）'
    )
    square_group.add_argument(
        '-center', 
        nargs=3, 
        type=int, 
        metavar=('center_x', 'center_y', 'side_length'),
        help='通过中心点和边长绘制正方形'
    )
    
    return square_parser