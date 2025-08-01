import time
import subprocess
import pyautogui

from src.main.python.terminal_logger.logger import info, warn, error

from src.main.python.configs import drawer_panel_config, screen_config
from src.main.python.utils.auto_speed_manager import auto_speed_config


# ======================
# 通用功能方法
# ======================

def open_paint():
    """
    打开画图工具并最大化窗口
    
    Step:
    1. 启动画图工具
    2. 最大化窗口
    3. 进入图层模式
    4. 显示系统兼容性提示
    """
    # Step 1: 启动画图工具
    subprocess.Popen("mspaint")
    info(True, "正在启动画图工具...", True)
    time.sleep(2)  # 等待画图启动
    
    # Step 2: 最大化窗口
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('x')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待窗口最大化
    info(True, "画图工具已最大化", True)

    # Step 3: 进入图层模式
    enter_layer_mode()

    # Step 4: 显示系统兼容性提示
    warn(True, "此脚本使用的画图软件为 Win11 系统自带的画图软件", True)

def minimize_paint():
    """
    最小化画图工具窗口

    Step:
    1. 激活画图窗口
    2. 发送最小化快捷键
    """
    activate_window()
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('n')
    info(True, "画图工具已最小化", True)

def activate_window():
    """
    激活画图窗口，确保其处于活动状态
    
    Step:
    1. 点击激活窗口
    """
    # Step 1: 点击激活窗口
    info(False, "激活画图窗口...", True)
    pyautogui.click(screen_config.WINDOW_ACTIVATE_POSITION)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待窗口响应
    info(False, "画图窗口已激活", True)

def activate_canvas():
    """
    激活画布，确保处于绘图模式
    取消选中上一次的绘图对象
    
    Step:
    1. 点击
    """
    # Step 1: 点击
    pyautogui.click(screen_config.CANVAS_BLANK_POSITION)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待画布响应
    info(False, "画布已激活", True)

def click_shapes_button():
    """
    点击形状按钮（通用功能）
    
    Step:
    1. 激活窗口确保操作正确
    2. 计算形状按钮位置
    3. 点击形状按钮
    """
    # Step 1: 激活窗口确保操作正确
    activate_window()
    
    # Step 2: 计算形状按钮位置
    shapes_button_x, shapes_button_y = drawer_panel_config.SHAPES_BUTTON_POSITION
    if shapes_button_x is None or shapes_button_y is None:
        error(True, "形状按钮位置未设置", True)
    
    # Step 3: 点击形状按钮
    pyautogui.click(x=shapes_button_x, y=shapes_button_y)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待按钮响应
    info(False, "已点击形状按钮", True)

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
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待按钮响应

    # Step 3: 等待界面切换
    info(True, "已进入图层模式", True)

def enter_color_mode():
    """
    进入颜色填充模式

    Step:
    1. 激活窗口确保操作正确
    2. 点击颜料桶按钮
    3. 等待界面切换
    """
    # Step 1: 激活窗口确保操作正确
    activate_window()

    # Step 2: 点击颜料桶按钮
    colors_button_x, colors_button_y = drawer_panel_config.FILL_TOOL_POSITION
    if colors_button_x is None or colors_button_y is None:
        error(True, "颜料桶按钮位置未设置", True)
        return

    pyautogui.click(x=colors_button_x, y=colors_button_y)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待按钮响应

    # Step 3: 等待界面切换
    info(False, "已进入颜色填充模式", True)

def select_color(color: str) -> None:
    """
    选择指定的颜色

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