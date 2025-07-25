import time
import pyautogui

from src.main.python.auto_drawer.utils.canvas_tools import enter_color_mode, activate_canvas, select_color
from src.main.python.utils.auto_speed_manager import auto_speed_config

from src.main.python.terminal_logger.logger import info


def select_fill_tool():
    """
    选择填充工具（colorer 层接口）

    Step:
    1. 进入颜色模式
    """
    # Step 1: 进入颜色模式
    enter_color_mode()
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待颜色模式激活

def fill_color(color: str, x: int, y: int):
    """
    在指定坐标处进行颜色填充

    参数:
        color (str): 填充颜色名称或代码
        x (int): 填充点的X坐标
        y (int): 填充点的Y坐标

    Step:
    """
    activate_canvas()  # 确保画布处于活动状态
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待画布激活

    # Step 3: 移动鼠标到指定位置并点击填充
    pyautogui.moveTo(x, y)  # 移动鼠标到指定位置
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待鼠标移动完成
    pyautogui.click()
    info(False, f"在 ({x}, {y}) 位置填充颜色: {color}", True)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待填充完成
    

def choose_color(color: str):
    """
    选择指定颜色（colorer 层接口）

    参数:
        color (str): 颜色名称或代码

    Step:
    1. 选择指定颜色
    """
    # Step 1: 选择指定颜色
    select_color(color)