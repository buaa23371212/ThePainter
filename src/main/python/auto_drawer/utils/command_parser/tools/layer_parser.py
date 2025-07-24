from src.main.python.auto_drawer.utils.command_parser.tools import LAYER_OPERATIONS_CHOICES

def add_new_layer_arguments(subparsers):
    """为添加新图层命令添加参数解析"""
    new_layer_parser = subparsers.add_parser('add_layer', help='添加新图层')
    
    return new_layer_parser

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

def add_layer_operation_arguments(subparsers):
    """为图层操作命令添加参数解析"""
    layer_operation_parser = subparsers.add_parser('layer_operation', help='对指定图层执行操作')
    layer_operation_parser.add_argument(
        '-operation',
        type=str,
        required=True,
        metavar='OPERATION',
        choices=LAYER_OPERATIONS_CHOICES,
        help='要执行的图层操作'
    )
    layer_operation_parser.add_argument(
        '-layer_id',
        type=int,
        default=1,
        metavar='LAYER_ID',
        help='要操作的图层ID，默认为1（顶部图层）'
    )
    
    return layer_operation_parser