import time
import pyautogui
from .utils import click_shapes_button, activate_canvas

# ======================
# 专用功能方法
# ======================

def select_circle_tool():
    """选择圆形工具"""
    click_shapes_button()
    pyautogui.press('right', presses=2)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    activate_canvas()

def draw_circle(start_x, start_y, end_x, end_y):
    """绘制圆形（通过起点和终点）"""
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    time.sleep(0.2)
    pyautogui.keyDown('shift')
    pyautogui.dragTo(end_x, end_y, duration=0.5)
    pyautogui.keyUp('shift')
    print(f"[INFO] 成功绘制圆形 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))")

def draw_circle_by_center(center_x, center_y, radius):
    """绘制圆形（通过圆心和半径）"""
    start_x = center_x - radius
    start_y = center_y - radius
    end_x = center_x + radius
    end_y = center_y + radius
    draw_circle(start_x, start_y, end_x, end_y)
    print(f"[INFO] 成功绘制圆形 (圆心: ({center_x}, {center_y}), 半径: {radius})")