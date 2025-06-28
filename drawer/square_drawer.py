import os
import time
import pyautogui
from ..tool.utils import activate_canvas, click_shapes_button

# ======================
# 专用功能方法
# ======================

def select_rectangle_tool():
    """
    在画图工具中选择矩形工具
    """
    # print("[INFO] 选择矩形工具...")
    
    # Step 1: 点击形状按钮
    click_shapes_button()

    # Step 2: 选择矩形工具
    # 通常圆形工具的下一个就是矩形工具
    pyautogui.press('right', presses=3)  # 按右方向键3次选择矩形工具
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    # print("[INFO] 已选择矩形工具")
    
    # Step 3: 激活画布确保进入绘图模式
    activate_canvas()

def draw_square(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制正方形
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    # print(f"[INFO] 开始绘制正方形 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))")
    
    # Step 1: 缓慢移动到起始位置
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    time.sleep(0.2)  # 额外延迟确保识别
    
    # Step 2: 按住Shift键绘制正方形
    pyautogui.keyDown('shift')
    pyautogui.dragTo(end_x, end_y, duration=0.5)
    pyautogui.keyUp('shift')
    
    # print("[INFO] 成功绘制正方形！")

def draw_square_by_center(center_x, center_y, side_length):
    """
    通过中心和边长绘制正方形
    
    参数:
        center_x (int): 中心点X坐标
        center_y (int): 中心点Y坐标
        side_length (int): 正方形边长
    """
    # Step 1: 计算起始点和结束点
    start_x = center_x - side_length // 2
    start_y = center_y - side_length // 2
    end_x = center_x + side_length // 2
    end_y = center_y + side_length // 2
    
    # Step 2: 调用绘制函数
    draw_square(start_x, start_y, end_x, end_y)

# ======================
# 导出函数供主程序调用
# ======================

def draw_square_command(args):
    """处理正方形绘制命令"""
    if args.bounding:
        start_x, start_y, end_x, end_y = args.bounding
        draw_square(start_x, start_y, end_x, end_y)
    elif args.center:
        center_x, center_y, side_length = args.center
        draw_square_by_center(center_x, center_y, side_length)
    else:
        # 默认行为：在屏幕中心绘制正方形
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        draw_square_by_center(center_x, center_y, 200)