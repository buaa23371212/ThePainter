import pyautogui

from utils.tools.color_tools import select_color
from utils.tools.tools import enter_color_mode

def fill_color(color: str, x: int, y: int):
    """
    在指定坐标处进行颜色填充

    参数:
        color (str): 填充颜色名称或代码
        x (int): 填充点的X坐标
        y (int): 填充点的Y坐标

    Step:
    1. 选择指定颜色
    2. 移动鼠标到指定坐标
    3. 执行点击进行填充
    """
    # Step 1: 选择指定颜色
    enter_color_mode()  # 确保进入颜色选择模式
    select_color(color)

    # Step 2: 移动鼠标到指定坐标
    pyautogui.moveTo(x, y)

    # Step 3: 执行点击进行填充
    pyautogui.click()