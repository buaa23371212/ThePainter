import time
import pyautogui

from public_utils.terminal_logger.logger import info, error

from configs import auto_speed_config, drawer_panel_config
from auto_drawer.src.utils.canvas_tools import activate_window

def add_layer():
    """
    添加新图层

    前置条件：
    - 必须已进入图层模式

    Step:
    1. 激活窗口确保操作正确
    2. 点击添加图层按钮

    结果说明：
    - 新增加的图层会出现在图层列表的最上层（顶部）。
    """
    # Step 1: 激活窗口确保操作正确
    activate_window()

    # Step 2: 点击添加图层按钮
    pyautogui.click(drawer_panel_config.ADD_LAYER_BUTTON_POSITION)

    info(False, "已添加新图层，新图层位于最上层", True)

def select_layer(layer_index):
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
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待按钮响应

    # Step 3: 敲击(index - 1)下方向键
    for _ in range(layer_index - 1):
        pyautogui.press('down')
        time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待每次按键响应

    info(False, f"已选择图层 {layer_index}", True)

def get_layer_view_position(layer_index: int) -> tuple:
    """
    根据图层索引计算该图层在视图中的坐标位置

    Step:
    1. 获取第一个图层的基准坐标
    2. 计算每个图层的垂直偏移量（通常等于图层视图高度）
    3. 返回目标图层的坐标

    :param layer_index: 图层索引（1为顶部图层）
    :return: (x, y) 坐标元组
    """
    base_x, base_y = drawer_panel_config.FIRST_LAYER_VIEW_POSITION
    offset = (layer_index - 1) * drawer_panel_config.LAYER_VIEW_HEIGHT
    return (base_x, base_y + offset)

def select_layer_operation(operation: str, layer_index: int = 1):
    """
    执行图层操作

    前置条件：
    - 必须已选中一个目标图层，否则操作无效。

    Step:
    1. 计算目标图层的视图位置
    2. 右键点击目标图层视图
    3. 根据操作类型选择对应的操作
    4. 按enter键确认操作
    """
    # Step 1: 计算目标图层的视图位置
    layer_view_position = get_layer_view_position(layer_index)

    # Step 2: 右键点击目标图层视图
    pyautogui.rightClick(layer_view_position)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待右键菜单弹出

    # Step 3: 根据操作类型选择对应的操作
    # 1. 获取操作对应的按下方向键次数
    key_presses = drawer_panel_config.get_tab_key_presses(operation)
    if key_presses == -1:
        error(False, f"未知的图层操作: {operation}", True)
        return
    
    # 2. 如果key_presses > 0，按下方向键选择操作
    if key_presses > 0:
        for _ in range(key_presses):
            pyautogui.press('down')
            time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待每次按键响应
    
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待操作响应

    # Step 4: 按enter键确认操作
    pyautogui.press('enter')