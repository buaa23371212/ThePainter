import time
import pyautogui

from utils.tools.color_tools import select_color
from utils.tools.tools import enter_color_mode, activate_canvas
from utils.config import auto_speed_config
from terminal_logger.logger import info, warn, error, debug

def fill_color(color: str, x: int, y: int):
    """
    在指定坐标处进行颜色填充

    参数:
        color (str): 填充颜色名称或代码
        x (int): 填充点的X坐标
        y (int): 填充点的Y坐标

    Step:
    1. 进入颜色填充模式
    2. 选择指定颜色
    3. 执行点击进行填充
    """
    # Step 1: 进入颜色填充模式
    enter_color_mode()

    # Step 2: 选择指定颜色
    select_color(color)

    # Step 3: 执行点击进行填充
    activate_canvas()  # 确保画布处于活动状态
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待画布激活
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