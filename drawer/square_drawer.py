import pyautogui
from drawer.rectangle_drawer import select_rectangle_tool, draw_rectangle

# ======================
# 专用功能方法
# ======================

def select_square_tool():
    """
    在画图工具中选择正方形工具
    """
    select_rectangle_tool()

def draw_square(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制正方形
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    draw_rectangle(start_x, start_y, end_x, end_y)

def draw_square_by_center(center_x, center_y, size):
    """
    通过中心点和尺寸绘制正方形
    
    参数:
        center_x (int): 中心点X坐标
        center_y (int): 中心点Y坐标
        size (int): 正方形的边长
    """
    # Step 1: 计算起始点和结束点
    start_x = center_x - size // 2
    start_y = center_y - size // 2
    end_x = center_x + size // 2
    end_y = center_y + size // 2
    
    # Step 2: 调用绘制函数
    draw_rectangle(start_x, start_y, end_x, end_y)

# ======================
# 导出函数供主程序调用
# ======================

def draw_square_command(args):
    """处理正方形绘制命令"""
    if args.bounding:
        start_x, start_y, end_x, end_y = args.bounding
        draw_square(start_x, start_y, end_x, end_y)
    elif args.center:
        center_x, center_y, size = args.center
        draw_square_by_center(center_x, center_y, size)
    else:
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        size = 100  # 默认边长
        draw_square_by_center(center_x, center_y, size)