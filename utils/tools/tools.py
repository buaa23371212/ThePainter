import time
import subprocess
import pyautogui

from terminal_logger.logger import info, warn, error

from utils.config import screen_config, auto_speed_config, drawer_panel_config

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


def activate_window():
    """
    激活画图窗口，确保其处于活动状态
    
    Step:
    1. 点击左上角激活窗口
    """
    # Step 1: 点击左上角激活窗口
    info(False, "激活画图窗口...", True)
    pyautogui.click(screen_config.WINDOW_ACTIVATE_POSITION)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待窗口响应
    info(False, "画图窗口已激活", True)

def activate_canvas():
    """
    激活画布，确保处于绘图模式
    
    Step:
    1. 计算屏幕中心
    2. 点击画布中心
    """
    # Step 1: 计算屏幕中心
    info(False, "激活画布...", True)
    
    screen_width = screen_config.SCREEN_WIDTH
    screen_height = screen_config.SCREEN_HEIGHT
    if screen_width is None or screen_height is None:
        error(True, "屏幕宽高未设置", True)
    
    # Step 2: 点击画布中心
    pyautogui.click(screen_config.CANVAS_CENTER)
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