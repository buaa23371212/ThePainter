from auto_drawer.src.utils.drawer.line_drawer import draw_line, select_line_tool
from auto_drawer.src.utils.data_processor import convert_points_to_coords, validate_shape_args

from public_utils.terminal_logger.logger import info, error

# ======================
# 专用功能方法
# ======================
def draw_polyline(points):
    """
    绘制多段折线

    前置条件
    - 确保已验证参数合法性

    参数:
        points (list): 折线的顶点列表，每个顶点是一个包含两个元素的列表 [x, y]
    """
    for i in range(len(points) - 1):
        start_x, start_y = points[i]
        end_x, end_y = points[i + 1]
        draw_line(start_x, start_y, end_x, end_y)


# ======================
# 参数验证
# ======================
def validate_point_count(points):
    if points:
        if len(points) < 3:
            raise ValueError("折线至少需要6个坐标值（3个点）")

def validate_polyline_args(args):
    """
    验证折线参数的有效性

    Step:

    参数:
        args: 命令行参数对象
    """
    validate_shape_args(args)


# ======================
# 导出函数供主程序调用
# ======================
def select_polyline_tool():
    select_line_tool()

def draw_polyline_command(args):
    """
    执行绘制多段折线的命令

    参数:
        args: 解析后的命令行参数，其中 args.points 应该是一个包含多个顶点的列表
    """
    try:
        # Step 1: 验证参数
        validate_polyline_args(args)

        points = []

        # Step 2: 获取点数据
        if args.points:
            # 转换点列表为坐标元组
            points = convert_points_to_coords(args.points)

        validate_point_count(points)

        # Step 3: 绘制曲线
        draw_polyline(points)

    except Exception as e:
        error(True, f"绘制曲线失败: {str(e)}", True)