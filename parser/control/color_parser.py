def add_color_parser(parser):
    """
    Add color parser to the given parser.
    """
    parser.add_argument(
        "-color",
        type=str,
        help="The color to use for filling. 若未指定则使用当前颜色。",
        choices=[
            "black", "white", "red", "green", "blue", "yellow",
            "gray", "lightgray", "darkgray", "orange", "purple", "brown"
        ]
    )

def add_fill_arguments(subparsers):
    """
    为填充命令添加参数解析
    命令格式: fill -color <颜色> -x <X坐标> -y <Y坐标>
    """
    fill_parser = subparsers.add_parser('fill', help='对指定位置进行颜色填充')
    fill_parser.add_argument(
        '-color',
        type=str,
        required=True,
        choices=[
            "black", "white", "red", "green", "blue", "yellow",
            "gray", "lightgray", "darkgray", "orange", "purple", "brown"
        ],
        help='填充颜色'
    )
    fill_parser.add_argument(
        '-x',
        type=int,
        required=True,
        metavar='X_COORD',
        help='填充点的X坐标'
    )
    fill_parser.add_argument(
        '-y',
        type=int,
        required=True,
        metavar='Y_COORD',
        help='填充点的Y坐标'
    )
    return fill_parser