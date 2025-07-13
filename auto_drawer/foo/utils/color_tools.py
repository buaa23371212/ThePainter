import time
import pyautogui

from auto_drawer.foo.configs import drawer_panel_config, auto_speed_config
from auto_drawer.foo.utils.general_tools import activate_window

from utils.terminal_logger.logger import info

def select_color(color: str) -> None:
    """
    选择指定的颜色

    前置条件
    - 确保已进入颜色填充模式

    Step:
    1. 激活窗口确保操作正确
    2. 点击第一个颜色视图
    3. 通过color获取presses次数，敲击右方向键选择颜色
    4. 点击确认按钮
    """
    # Step 1: 激活窗口确保操作正确
    activate_window()

    # Step 2: 点击第一个颜色视图
    pyautogui.click(drawer_panel_config.FILL_COLOR_POSITION)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待按钮响应

    # Step 3: 通过color获取presses次数，敲击右方向键选择颜色
    presses = drawer_panel_config.get_fill_color_presses(color)
    if presses == -1:
        raise ValueError(f"颜色 '{color}' 不在预设列表中")
    # presses次数为0时不需要敲击
    if presses > 0:
        pyautogui.press('right', presses=presses)
        time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待颜色选择

    # Step 4: 点击确认按钮
    pyautogui.press('enter')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待按钮响应
    info(False, f"已选择颜色: {color}", True)