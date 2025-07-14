def add_polyline_arguments(subparsers):
    polyline_parser = subparsers.add_parser('polyline', help='绘制多段折线')
    polyline_group = polyline_parser.add_mutually_exclusive_group(required=True)

    polyline_group.add_argument(
        '-points',
        nargs='+',
        type=int
    )