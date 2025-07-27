def add_polygon_arguments(subparsers):
    """为多边形命令添加参数解析"""
    polygon_parser = subparsers.add_parser('polygon', help='绘制任意多边形')
    
    # 顶点来源选项组（文件或直接坐标）
    source_group = polygon_parser.add_mutually_exclusive_group(required=True)
    
    # 文件方式选项
    source_group.add_argument(
        '-file', 
        type=str,
        metavar='FILE_PATH',
        help='包含多边形定义的JSON文件路径'
    )
    
    # 直接坐标选项
    source_group.add_argument(
        '-points', 
        nargs='+', 
        type=int,
        metavar=('X', 'Y'),
        help='直接指定多边形的顶点坐标（每两个整数表示一个顶点）'
    )
    
    # 文件引用方式选项组（ID或名称）
    ref_group = polygon_parser.add_mutually_exclusive_group()
    
    ref_group.add_argument(
        '-id', 
        type=str,
        metavar='POLYGON_ID',
        help='JSON文件中多边形的ID标识符'
    )
    
    ref_group.add_argument(
        '-name', 
        type=str,
        metavar='POLYGON_NAME',
        help='JSON文件中多边形的名称'
    )
    
    return polygon_parser