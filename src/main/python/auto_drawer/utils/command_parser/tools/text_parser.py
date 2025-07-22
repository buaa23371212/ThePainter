def add_text_arguments(subparsers):
    """
    添加文本相关的命令行参数解析器
    """
    text_parser = subparsers.add_parser('text', help='输入文本到指定位置')
    text_parser.add_argument('-text', type=str, required=True, help='要输入的文本内容')
    text_parser.add_argument('-x', type=int, required=True, help='文本输入的X坐标')
    text_parser.add_argument('-y', type=int, required=True, help='文本输入的Y坐标')
    return text_parser