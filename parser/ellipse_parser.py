def add_ellipse_arguments(subparsers):
    """为椭圆命令添加参数解析"""
    ellipse_parser = subparsers.add_parser('ellipse', help='绘制椭圆')
    ellipse_group = ellipse_parser.add_mutually_exclusive_group()

    ellipse_group.add_argument(
        '-bounding',
        nargs=4,
        type=int,
        metavar=('start_x', 'start_y', 'end_x', 'end_y'),
        help='通过起点和终点绘制椭圆（四个整数坐标）'
    )
    ellipse_group.add_argument(
        '-center',
        nargs=4,
        type=int,
        metavar=('center_x', 'center_y', 'semi_major_axis', 'semi_minor_axis'),
        help='通过中心点、长半轴和短半轴绘制椭圆'
    )

    return ellipse_parser