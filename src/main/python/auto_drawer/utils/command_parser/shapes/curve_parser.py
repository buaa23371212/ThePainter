def add_curve_arguments(subparsers):
    """为曲线命令添加参数解析"""
    curve_parser = subparsers.add_parser('curve', help='绘制三次贝塞尔曲线')
    
    # 曲线来源选项组（文件或直接坐标）
    source_group = curve_parser.add_mutually_exclusive_group(required=True)
    
    # 文件方式选项
    source_group.add_argument(
        '-file', 
        type=str,
        metavar='FILE_PATH',
        help='包含曲线定义的JSON文件路径'
    )
    
    # 直接坐标选项
    source_group.add_argument(
        '-points', 
        nargs=8, 
        type=int,
        metavar=('X0', 'Y0', 'X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3'),
        help='直接指定曲线的四个点（起点、控制点1、控制点2、终点），共8个整数'
    )
    
    # 文件引用方式选项组（ID或名称）
    ref_group = curve_parser.add_mutually_exclusive_group()
    
    ref_group.add_argument(
        '-id', 
        type=str,
        metavar='CURVE_ID',
        help='JSON文件中曲线的ID标识符'
    )
    
    ref_group.add_argument(
        '-name', 
        type=str,
        metavar='CURVE_NAME',
        help='JSON文件中曲线的名称'
    )
    
    return curve_parser


def add_multicurve_arguments(subparsers):
    """为多段曲线命令添加参数解析"""
    multicurve_parser = subparsers.add_parser('multicurve', help='绘制多段贝塞尔曲线')
    
    # 曲线来源选项组（文件或直接坐标）
    source_group = multicurve_parser.add_mutually_exclusive_group(required=True)
    
    # 文件方式选项
    source_group.add_argument(
        '-file', 
        type=str,
        metavar='FILE_PATH',
        help='包含多段曲线定义的JSON文件路径'
    )
    
    # 直接坐标选项
    source_group.add_argument(
        '-points', 
        nargs='+', 
        type=int,
        metavar=('X', 'Y'),
        help='直接指定多段曲线的点序列（每两个整数表示一个点）'
    )
    
    # 文件引用方式选项组（ID或名称）
    ref_group = multicurve_parser.add_mutually_exclusive_group()
    
    ref_group.add_argument(
        '-id', 
        type=str,
        metavar='MULTICURVE_ID',
        help='JSON文件中多段曲线的ID标识符'
    )
    
    ref_group.add_argument(
        '-name', 
        type=str,
        metavar='MULTICURVE_NAME',
        help='JSON文件中多段曲线的名称'
    )
    
    return multicurve_parser