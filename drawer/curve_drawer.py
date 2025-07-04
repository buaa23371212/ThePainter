import time
import pyautogui

from utils.tools.tools import click_shapes_button, activate_canvas
from utils.config import auto_speed_config

from drawer.line_drawer import draw_line

from terminal_logger.logger import info

# ======================
# 专用功能方法
# ======================
def select_curve_tool():
    """
    在画图工具中选择曲线工具
    """
    # 使用info函数记录日志，但show=False不显示输出
    info(False, "选择曲线工具...", True)
    
    # Step 1: 点击形状按钮
    click_shapes_button()
    
    # Step 2: 选择曲线工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    pyautogui.press('right')  # 右键切换到曲线工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待工具选择完成
    info(False, "已选择曲线工具", True)

def draw_curve(start_x, start_y, control_x, control_y, end_x, end_y):
    """
    在画图工具中绘制曲线
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        control_x (int): 控制点X坐标
        control_y (int): 控制点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    # 使用info函数记录日志，但show=False不显示输出
    info(False, f"开始绘制曲线 (起点: ({start_x}, {start_y}), 控制点: ({control_x}, {control_y}), 终点: ({end_x}, {end_y}))", True)
    activate_canvas()
    
    # Step 1: 画直线
    draw_line(start_x, start_y, end_x, end_y)

    # Step 2: 点击控制点
    pyautogui.moveTo(control_x, control_y, duration=auto_speed_config.ACTUAL_MOUSE_MOVE_SPEED)
    time.sleep(auto_speed_config.ACTUAL_EXTRA_MOVE_DELAY)  # 额外延迟确保识别
    pyautogui.click()
    
    info(False, "成功绘制曲线！", True)

# ======================
# 导出函数供主程序调用
# ======================
def draw_curve_command(args):
    # TODO: 实现命令行参数解析和调用绘制曲线函数 
    pass