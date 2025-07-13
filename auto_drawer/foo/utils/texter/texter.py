import time
import pyautogui

from auto_drawer.foo.utils.general_tools import activate_canvas, activate_window
from auto_drawer.foo.configs import drawer_panel_config, auto_speed_config

from utils.terminal_logger.logger import info, error

def select_texter_tool():
    """
    选择文本工具（texter 层接口）

    Step:
    """
    # Step 1: 进入文本工具模式
    activate_window()  # 确保窗口处于活动状态
    pyautogui.click(drawer_panel_config.TEXT_TOOL_POSITION)
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待工具激活
    info(False, "已选择文本工具", True)

def create_text(text: str, x: int, y: int):
    """
    创建文本

    前置条件：
    - 必须已选择文本工具

    Step:
    1. 激活窗口确保操作正确
    2. 点击画布上的指定位置
    3. 输入文本内容
    4. 按下回车键确认输入
    """
    # Step 1: 激活窗口确保操作正确
    activate_canvas()

    # Step 2: 双击击画布上的指定位置
    if x is None or y is None:
        error(True, "文本位置未设置", True)
        return
    pyautogui.moveTo(x=x, y=y)                          # 指定位置
    pyautogui.click(clicks=2)                           # 双击以创建文本框
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)     # 等待点击响应

    # Step 3: 输入文本内容
    pyautogui.write(text, interval=0.05)                # 模拟键盘输入，间隔0.05秒

    # Step 4: 按下回车键确认输入
    pyautogui.press('enter')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)     # 等待文本创建完成
    info(False, f"已创建文本: {text}", True)