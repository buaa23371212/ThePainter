import pyautogui

from src.main.python.auto_drawer.utils.drawer.ellipse_drawer import select_ellipse_tool, draw_ellipse

# ======================
# 专用功能方法
# ======================
def draw_circle(start_x, start_y, end_x, end_y):
    draw_ellipse(start_x, start_y, end_x, end_y)

def draw_circle_by_center(center_x, center_y, radius):
    """
    通过中心点和尺寸绘制椭圆
    
    参数:
        center_x (int): 中心点X坐标
        center_y (int): 中心点Y坐标
        radius (int): 圆的半径
    """
    # Step 1: 计算起始点和结束点
    start_x = center_x - radius // 2
    start_y = center_y - radius // 2
    end_x = center_x + radius // 2
    end_y = center_y + radius // 2
    
    # Step 2: 调用绘制函数
    draw_ellipse(start_x, start_y, end_x, end_y)

# ======================
# 导出函数供主程序调用
# ======================
def select_circle_tool():
    select_ellipse_tool()

def draw_circle_command(args):
    """处理圆形绘制命令"""
    if args.bounding:
        start_x, start_y, end_x, end_y = args.bounding
        draw_circle(start_x, start_y, end_x, end_y)
    elif args.center:
        center_x, center_y, radius = args.center
        draw_circle_by_center(center_x, center_y, radius)
    else:
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        radius = 100 # 默认半径
        draw_circle_by_center(center_x, center_y, radius)