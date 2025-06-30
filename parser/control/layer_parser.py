def add_layer_choose_arguments(subparsers):
    """为选择图层命令添加参数解析"""
    layer_parser = subparsers.add_parser('choose_layer', help='选择指定的图层')
    layer_parser.add_argument(
        '-layer_id',
        type=int,
        required=True,
        metavar='LAYER_ID',
        help='要选择的图层ID'
    )
    
    return layer_parser