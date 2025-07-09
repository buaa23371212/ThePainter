import time
import pyautogui

from painter_tools.painter_config import drawer_panel_config, auto_speed_config
from painter_tools.painter_tools.general_tools import activate_window

from terminal_logger.logger import info, error

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