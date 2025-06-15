import time
import pyautogui
from .utils import click_shapes_button, activate_canvas

# ======================
# 专用功能方法
# ======================

def select_circle_tool():
    """
    在画图工具中选择圆形工具
    """
    # print("[INFO] 选择圆形工具...")
    
    # Step 1: 点击形状按钮
    click_shapes_button()
    
    # Step 2: 选择圆形工具
    pyautogui.press('right', presses=2)  # 按右方向键2次选择圆形
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    # print("[INFO] 已选择圆形工具")
    
    # Step 3: 激活画布
    activate_canvas()

def draw_circle(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制圆形
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    # print(f"[INFO] 开始绘制圆形 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))")
    
    # Step 1: 缓慢移动到起始位置
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    time.sleep(0.2)  # 额外延迟确保识别
    
    # Step 2: 按住Shift键绘制正圆
    pyautogui.keyDown('shift')
    pyautogui.dragTo(end_x, end_y, duration=0.5)
    pyautogui.keyUp('shift')
    
    # print("[INFO] 成功绘制圆形！")

def draw_circle_by_center(center_x, center_y, radius):
    """
    通过圆心和半径绘制圆形
    
    参数:
        center_x (int): 圆心X坐标
        center_y (int): 圆心Y坐标
        radius (int): 圆半径
    """
    # Step 1: 计算起始点和结束点
    start_x = center_x - radius
    start_y = center_y - radius
    end_x = center_x + radius
    end_y = center_y + radius
    
    # Step 2: 调用绘制函数
    draw_circle(start_x, start_y, end_x, end_y)