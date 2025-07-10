def add_square_arguments(subparsers):
    """
    添加正方形绘制相关的命令行参数
    """
    square_parser = subparsers.add_parser('square', help='绘制正方形')
    
    # 添加边界参数
    square_parser.add_argument(
        '-bounding',
        nargs=4,
        type=int,
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        help='通过起始点和结束点坐标绘制正方形'
    )
    
    # 添加中心点和尺寸参数
    square_parser.add_argument(
        '-center',
        nargs=3,
        type=int,
        metavar=('center_x', 'center_y', 'size'),
        help='通过中心点和尺寸绘制正方形'
    )
    
    return square_parser