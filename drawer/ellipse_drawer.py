import time
import pyautogui
from tool.utils import click_shapes_button, activate_canvas
from terminal_logger.logger import info

# ======================
# 专用功能方法
# ======================

def select_ellipse_tool():
    """
    在画图工具中选择椭圆工具
    """
    info(False, "选择椭圆工具...", True)
    
    # Step 1: 点击形状按钮
    click_shapes_button()
    
    # Step 2: 选择椭圆工具
    pyautogui.press('right', presses=2)  # 假设按右方向键2次选择椭圆工具，具体根据实际情况调整
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    info(False, "已选择椭圆工具", True)
    
    # Step 3: 激活画布
    activate_canvas()

def draw_ellipse(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制椭圆
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    info(False, f"开始绘制椭圆 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))", True)
    
    # Step 1: 缓慢移动到起始位置
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    time.sleep(0.2)  # 额外延迟确保识别
    
    # Step 2: 绘制椭圆
    pyautogui.dragTo(end_x, end_y, duration=0.5)
    
    info(False, "成功绘制椭圆！", True)

def draw_ellipse_by_center(center_x, center_y, width, height):
    """
    通过中心点和尺寸绘制椭圆
    
    参数:
        center_x (int): 中心点X坐标
        center_y (int): 中心点Y坐标
        width (int): 椭圆宽度
        height (int): 椭圆高度
    """
    # Step 1: 计算起始点和结束点
    start_x = center_x - width // 2
    start_y = center_y - height // 2
    end_x = center_x + width // 2
    end_y = center_y + height // 2
    
    # Step 2: 调用绘制函数
    draw_ellipse(start_x, start_y, end_x, end_y)

# ======================
# 导出函数供主程序调用
# ======================

def draw_ellipse_command(args):
    """处理椭圆绘制命令"""
    if args.bounding:
        start_x, start_y, end_x, end_y = args.bounding
        draw_ellipse(start_x, start_y, end_x, end_y)
    elif args.center:
        center_x, center_y, width, height = args.center
        draw_ellipse_by_center(center_x, center_y, width, height)
    else:
        # 默认行为：在屏幕中心绘制椭圆
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        draw_ellipse_by_center(center_x, center_y, 200, 100)