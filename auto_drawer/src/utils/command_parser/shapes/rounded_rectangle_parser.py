def add_rounded_rectangle_arguments(subparsers):
    """为圆角矩形命令添加参数解析"""
    rounded_rectangle_parser = subparsers.add_parser('rounded_rectangle', help='绘制圆角矩形')
    rounded_rectangle_group = rounded_rectangle_parser.add_mutually_exclusive_group()

    rounded_rectangle_group.add_argument(
        '-bounding',
        nargs=4,
        type=int,
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        help='通过起点和终点绘制圆角矩形（四个整数坐标）'
    )
    rounded_rectangle_group.add_argument(
        '-center',
        nargs=5,
        type=int,
        metavar=('center_x', 'center_y', 'width', 'height', 'radius'),
        help='通过中心点、长宽和圆角半径绘制圆角矩形'
    )

    return rounded_rectangle_parser