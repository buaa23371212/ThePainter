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
    1. 进入颜色填充模式
    2. 选择指定颜色
    3. 移动鼠标到指定坐标
    4. 执行点击进行填充
    """
    # Step 1: 进入颜色填充模式
    enter_color_mode()

    # Step 2: 选择指定颜色
    select_color(color)

    # Step 3: 移动鼠标到指定坐标
    pyautogui.moveTo(x, y)

    # Step 4: 执行点击进行填充
    pyautogui.click()

def choose_color(color: str):
    """
    选择指定颜色（colorer 层接口）

    参数:
        color (str): 颜色名称或代码

    Step:
    1. 进入颜色选择模式
    2. 选择指定颜色
    """
    # Step 1: 进入颜色选择模式
    enter_color_mode()

    # Step 2: 选择指定颜色
    select_color(color)