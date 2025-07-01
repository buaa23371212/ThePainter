def add_color_parser(parser):
    """
    Add color parser to the given parser.
    """
    # Add color parser
    parser.add_argument(
        "-color",
        type=str,
        default="black",
        help="The color to use for filling. Default is 'black'.",
        choices=[
            "black", "white", "red", "green", "blue", "yellow",
            "gray", "lightgray", "darkgray", "orange", "purple", "brown"
        ]
    )