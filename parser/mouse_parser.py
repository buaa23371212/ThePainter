"""为移动鼠标命令添加参数解析"""
def add_move_mouse_arguments(subparsers):
    """为移动鼠标命令添加参数解析"""
    move_mouse_parser = subparsers.add_parser('move_mouse', help='将鼠标移动到指定位置')
    move_mouse_parser.add_argument(
        '-x', 
        type=int, 
        required=True,
        metavar='X_COORD',
        help='目标位置的X坐标'
    )
    move_mouse_parser.add_argument(
        '-y', 
        type=int, 
        required=True,
        metavar='Y_COORD',
        help='目标位置的Y坐标'
    )
    
    return move_mouse_parser

def add_mouse_click_arguments(subparsers):
    """为鼠标点击命令添加参数解析"""
    mouse_click_parser = subparsers.add_parser('mouse_click', help='模拟鼠标点击')
    mouse_click_parser.add_argument(
        '-x', 
        type=int, 
        required=True,
        metavar='X_COORD',
        help='目标位置的X坐标'
    )
    mouse_click_parser.add_argument(
        '-y', 
        type=int, 
        required=True,
        metavar='Y_COORD',
        help='目标位置的Y坐标'
    )
    
    return mouse_click_parser

def add_right_click_arguments(subparsers):
    """为鼠标右键点击命令添加参数解析"""
    right_click_parser = subparsers.add_parser('right_click', help='在指定位置使用鼠标右键点击')
    right_click_parser.add_argument(
        '-x', 
        type=int, 
        required=True,
        metavar='X_COORD',
        help='目标位置的X坐标'
    )
    right_click_parser.add_argument(
        '-y', 
        type=int, 
        required=True,
        metavar='Y_COORD',
        help='目标位置的Y坐标'
    )
    
    return right_click_parser