import time
import pyautogui
from terminal_logger.logger import info, error
from utils.config import drawer_panel_config
from utils.config import auto_speed_config
from utils.tools.tools import activate_window

def choose_layer(layer_index):
    """
    选择指定的图层

    Step:
    1. 激活窗口确保操作正确
    2. 点击第一个图层视图
    3. 敲击(index - 1)下方向键
    """
    # Step 1: 激活窗口确保操作正确
    activate_window()

    # Step 2: 点击第一个图层视图
    pyautogui.click(drawer_panel_config.FIRST_LAYER_VIEW_POSITION)
    time.sleep(auto_speed_config.CLICK_WAIT)  # 等待按钮响应

    # Step 3: 敲击(index - 1)下方向键
    for _ in range(layer_index - 1):
        pyautogui.press('down')
        time.sleep(auto_speed_config.CLICK_WAIT)  # 等待每次按键响应

    info(False, f"已选择图层 {layer_index}", True)