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