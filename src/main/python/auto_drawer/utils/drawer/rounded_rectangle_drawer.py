import time
import pyautogui

from src.main.python.auto_drawer.utils.canvas_tools import click_shapes_button, activate_canvas
from src.main.python.configs import screen_config
from src.main.python.utils.auto_speed_manager import auto_speed_config
from src.main.python.configs.drawer_panel_config import get_shape_panel_presses

from src.main.python.terminal_logger.logger import info


# ======================
# 专用功能方法
# ======================
def draw_rounded_rectangle(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制圆角矩形
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    info(False, f"开始绘制圆角矩形 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))", True)
    activate_canvas()
    
    # Step 1: 缓慢移动到起始位置
    pyautogui.moveTo(start_x, start_y, duration=auto_speed_config.ACTUAL_MOUSE_MOVE_SPEED)
    time.sleep(auto_speed_config.ACTUAL_EXTRA_MOVE_DELAY)  # 额外延迟确保识别
    
    # Step 2: 绘制圆角矩形（不再按住Shift键）
    pyautogui.dragTo(end_x, end_y, duration=auto_speed_config.ACTUAL_DRAW_DURATION_1)
    
    info(False, "成功绘制圆角矩形！", True)

def draw_rounded_rectangle_by_center(center_x, center_y, width, height):
    """
    通过中心和尺寸绘制圆角矩形
    
    参数:
        center_x (int): 中心点X坐标
        center_y (int): 中心点Y坐标
        width (int): 矩形宽度
        height (int): 矩形高度
    """
    info(False, f"开始绘制圆角矩形 (中心: ({center_x}, {center_y}), 宽度: {width}, 高度: {height})", True)
    
    # 计算起始和结束坐标
    start_x = center_x - width // 2
    start_y = center_y - height // 2
    end_x = center_x + width // 2
    end_y = center_y + height // 2
    
    # 调用绘制方法
    draw_rounded_rectangle(start_x, start_y, end_x, end_y)


# ======================
# 导出函数供主程序调用
# ======================
def select_rounded_rectangle_tool():
    """
    在画图工具中选择圆角矩形工具
    """
    info(False, "选择圆角矩形工具...", True)

    # Step 1: 点击形状按钮
    click_shapes_button()

    # Step 2: 选择圆角矩形工具
    pyautogui.press('right', presses=get_shape_panel_presses("rounded_rectangle"))  # 按右方向键4次选择圆角矩形工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    pyautogui.press('enter')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待工具选择完成
    info(False, "已选择圆角矩形工具", True)

def draw_rounded_rectangle_command(args):
    """处理矩形绘制命令"""
    if args.bounding:
        start_x, start_y, end_x, end_y = args.bounding
        draw_rounded_rectangle(start_x, start_y, end_x, end_y)
    elif args.center:
        center_x, center_y, width, height = args.center
        draw_rounded_rectangle_by_center(center_x, center_y, width, height)
    else:
        # 默认行为：在屏幕中心绘制矩形
        screen_width, screen_height = screen_config.SCREEN_WIDTH, screen_config.SCREEN_HEIGHT
        center_x, center_y = screen_width // 2, screen_height // 2
        width, height = 200, 100 # 默认宽度和高度
        draw_rounded_rectangle_by_center(center_x, center_y, width, height)