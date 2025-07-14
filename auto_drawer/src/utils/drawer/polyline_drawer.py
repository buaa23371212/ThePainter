from auto_drawer.src.utils.drawer.line_drawer import draw_line

from public_utils.terminal_logger.logger import info

def draw_polyline(points):
    """
    绘制多段折线

    参数:
        points (list): 折线的顶点列表，每个顶点是一个包含两个元素的列表 [x, y]
    """
    if len(points) < 2:
        info(False, "至少需要两个点来绘制折线", True)
        return

    for i in range(len(points) - 1):
        start_x, start_y = points[i]
        end_x, end_y = points[i + 1]
        draw_line(start_x, start_y, end_x, end_y)


# ======================
# 导出函数供主程序调用
# ======================
def draw_polyline_command(args):
    """
    执行绘制多段折线的命令

    参数:
        args: 解析后的命令行参数，其中 args.points 应该是一个包含多个顶点的列表
    """
    if args.points:
        draw_polyline(args.points)
    else:
        info(False, "未提供折线的顶点坐标", True)