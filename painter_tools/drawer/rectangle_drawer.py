import time
import pyautogui

from painter_tools.painter_tools.general_tools import click_shapes_button, activate_canvas
from painter_tools.painter_config import auto_speed_config, screen_config
from painter_tools.painter_config.drawer_panel_config import get_shape_panel_presses

from painter_tools.terminal_logger.logger import info

# ======================
# 专用功能方法
# ======================

def select_rectangle_tool():
    """
    在画图工具中选择矩形工具
    """
    info(False, "选择矩形工具...", True)
    
    # Step 1: 点击形状按钮
    click_shapes_button()

    # Step 2: 选择矩形工具
    # 通常圆形工具的下一个就是矩形工具
    pyautogui.press('right', presses=get_shape_panel_presses("rectangle"))  # 按右方向键3次选择矩形工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    pyautogui.press('enter')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待工具选择完成
    info(False, "已选择矩形工具", True)
    

def draw_rectangle(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制矩形
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    info(False, f"开始绘制矩形 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))", True)
    
    activate_canvas()  # 确保画布处于活动状态
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待画布激活

    # Step 1: 缓慢移动到起始位置
    pyautogui.moveTo(start_x, start_y, duration=auto_speed_config.ACTUAL_MOUSE_MOVE_SPEED)
    time.sleep(auto_speed_config.ACTUAL_EXTRA_MOVE_DELAY)  # 额外延迟确保识别
    
    # Step 2: 绘制矩形
    pyautogui.dragTo(end_x, end_y, duration=auto_speed_config.ACTUAL_DRAW_DURATION)
    
    info(False, "成功绘制矩形！", True)

def draw_rectangle_by_center(center_x, center_y, width, height):
    """
    通过中心和尺寸绘制矩形
    
    参数:
        center_x (int): 中心点X坐标
        center_y (int): 中心点Y坐标
        width (int): 矩形宽度
        height (int): 矩形高度
    """
    # Step 1: 计算起始点和结束点
    start_x = center_x - width // 2
    start_y = center_y - height // 2
    end_x = center_x + width // 2
    end_y = center_y + height // 2
    
    # Step 2: 调用绘制函数
    draw_rectangle(start_x, start_y, end_x, end_y)

# ======================
# 导出函数供主程序调用
# ======================

def draw_rectangle_command(args):
    """处理矩形绘制命令"""
    if args.bounding:
        start_x, start_y, end_x, end_y = args.bounding
        draw_rectangle(start_x, start_y, end_x, end_y)
    elif args.center:
        center_x, center_y, width, height = args.center
        draw_rectangle_by_center(center_x, center_y, width, height)
    else:
        # 默认行为：在屏幕中心绘制矩形
        screen_width, screen_height = screen_config.SCREEN_WIDTH, screen_config.SCREEN_HEIGHT
        center_x, center_y = screen_width // 2, screen_height // 2
        draw_rectangle_by_center(center_x, center_y, 200, 150)  # 默认200x150矩形