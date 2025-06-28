import time
import subprocess
import pyautogui
from terminal_logger.logger import info, warn
from tool import screen_config

# ======================
# 通用功能方法
# ======================

def open_paint():
    """
    打开画图工具并最大化窗口
    
    Step:
    1. 启动画图工具
    2. 最大化窗口
    3. 显示系统兼容性提示
    """
    # Step 1: 启动画图工具
    subprocess.Popen("mspaint")
    info(True, "正在启动画图工具...", True)
    time.sleep(2)  # 等待画图启动
    
    # Step 2: 最大化窗口
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('x')
    time.sleep(1)
    info(True, "画图工具已最大化", True)

    # Step 3: 显示系统兼容性提示
    warn(True, "此脚本使用的画图软件为Win11系统自带的画图软件", True)


def activate_window():
    """
    激活画图窗口，确保其处于活动状态
    
    Step:
    1. 点击左上角激活窗口
    """
    # Step 1: 点击左上角激活窗口
    info(False, "激活画图窗口...", True)
    pyautogui.click(x=100, y=100)
    time.sleep(0.5)
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
        screen_width, screen_height = pyautogui.size()
    
    # Step 2: 点击画布中心
    pyautogui.click(x=screen_width//2, y=screen_height//2)
    time.sleep(0.5)
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
    screen_width, screen_height = pyautogui.size()
    shapes_button_x = screen_width // 4 + 65 
    shapes_button_y = 95  
    
    # Step 3: 点击形状按钮
    pyautogui.click(x=shapes_button_x, y=shapes_button_y)
    time.sleep(1)
    info(False, "已点击形状按钮", True)