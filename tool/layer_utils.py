import time
import pyautogui
from terminal_logger.logger import info, error
from tool import drawer_panel_config, auto_speed_config
from .utils import activate_window

def enter_layer_mode():
    """
    进入图层模式

    Step:
    1. 激活窗口确保操作正确
    2. 点击图层按钮
    3. 等待界面切换
    """
    # Step 1: 激活窗口确保操作正确
    activate_window()

    # Step 2: 点击图层按钮
    layers_button_x, layers_button_y = drawer_panel_config.LAYERS_BUTTON_POSITION
    if layers_button_x is None or layers_button_y is None:
        error(True, "图层按钮位置未设置", True)
        return

    pyautogui.click(x=layers_button_x, y=layers_button_y)
    time.sleep(auto_speed_config.CLICK_WAIT)  # 等待按钮响应

    # Step 3: 等待界面切换
    info(True, "已进入图层模式", True)

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