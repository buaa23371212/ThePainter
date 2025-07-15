def add_polyline_arguments(subparsers):
    polyline_parser = subparsers.add_parser('polyline', help='绘制多段折线')

    # 曲线来源选项组（文件或直接坐标）
    source_group = polyline_parser.add_mutually_exclusive_group(required=True)

    # 文件方式选项
    source_group.add_argument(
        '-file',
        type=str,
        metavar='FILE_PATH',
        help='包含折线定义的JSON文件路径'
    )

    # 直接坐标选项
    source_group.add_argument(
        '-points',
        nargs='+',
        type=int,
        metavar=('X', 'Y'),
        help='直接指定多段折线的点序列（每两个整数表示一个点）'
    )

    # 文件引用方式选项组（ID或名称）
    ref_group = polyline_parser.add_mutually_exclusive_group()

    ref_group.add_argument(
        '-id',
        type=str,
        metavar='POLYLINE_ID',
        help='JSON文件中折线的ID标识符'
    )

    ref_group.add_argument(
        '-name',
        type=str,
        metavar='POLYLINE_NAME',
        help='JSON文件中折线的名称'
    )

    return polyline_parser