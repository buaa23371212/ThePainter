import time
import pyautogui

from utils.tools.tools import click_shapes_button, activate_canvas
from utils.config import auto_speed_config

from drawer.line_drawer import draw_line

from terminal_logger.logger import info

# ======================
# 专用功能方法
# ======================
def select_curve_tool():
    """
    在画图工具中选择曲线工具
    """
    # 使用info函数记录日志，但show=False不显示输出
    info(False, "选择曲线工具...", True)
    
    # Step 1: 点击形状按钮
    click_shapes_button()
    
    # Step 2: 选择曲线工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    pyautogui.press('right')  # 右键切换到曲线工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)  # 等待工具选择完成
    info(False, "已选择曲线工具", True)


# ======================
# 导出函数供主程序调用
# ======================
def draw_curve_command(args):
    # TODO: 实现命令行参数解析和调用绘制曲线函数 
    # 起点、终点、与两个控制点
    pass