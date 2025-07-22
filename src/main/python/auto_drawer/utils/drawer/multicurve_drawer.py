from src.main.python.auto_drawer.utils.data_processor import load_shape_from_json, validate_shape_args
from src.main.python.auto_drawer.utils.drawer.curve_drawer import select_curve_tool, draw_curve
from src.main.python.terminal_logger.logger import warn, error


# ======================
# 专用功能方法
# ======================
def draw_multicurve(points):
    """
    绘制多段曲线

    前置条件
    - 确保已验证参数合法性

    参数:
        points (list): 折线的顶点列表，每个顶点是一个包含两个元素的列表 [x, y]
    """
    for i in range(0, len(points) - 3, 3):
        segment_points = points[i:i + 4]
        draw_curve(segment_points)

# ======================
# 曲线数据处理方法
# ======================
def load_multicurve_from_json(file_path, multicurve_id=None, multicurve_name=None):
    return load_shape_from_json(file_path, "multi-curves", multicurve_id, multicurve_name)


# ======================
# 参数验证
# ======================
def validate_point_count(points):
    if points:
        if len(points) < 4:
            raise ValueError("曲线至少需要8个坐标值（4个点）")
        if (len(points) - 1) % 3 != 0:
            warn(True, "存在多余的点", True)

def validate_multicurve_args(args):
    validate_shape_args(args)


# ======================
# 导出函数供主程序调用
# ======================
def select_multicurve_tool():
    select_curve_tool()

def draw_multicurve_command(args):
    try:
        # Step 1: 验证参数
        validate_multicurve_args(args)

        points = []

        # Step 2: 获取点数据
        if args.file:
            # 从JSON文件加载曲线
            points = load_multicurve_from_json(args.file, args.id, args.name)
        elif args.points:
            # 转换点列表为坐标元组
            # points = convert_points_to_coords(args.points)
            pass

        validate_point_count(points)

        # Step 3: 绘制曲线
        draw_multicurve(points)

    except Exception as e:
        error(True, f"绘制曲线失败: {str(e)}", True)