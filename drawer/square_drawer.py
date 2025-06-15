import os
import time
import pyautogui
# from .utils import activate_canvas, click_shapes_button
from utils import open_paint, activate_canvas, click_shapes_button  # 测试用

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
# 主功能方法
# ======================

def draw_square_in_paint():
    """
    主函数：在画图工具中绘制正方形
    """
    try:
        # Step 1: 打开画图工具
        open_paint()
        
        # Step 2: 选择矩形工具
        select_rectangle_tool()
        
        # Step 3: 定位画布中心
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        # print(f"[INFO] 屏幕分辨率: {screen_width}x{screen_height}, 画布中心: ({center_x}, {center_y})")
        
        # Step 4: 绘制正方形
        draw_square_by_center(center_x, center_y, 200)
        
        # print("[INFO] 画图工具保持打开状态")
    except Exception as e:
        print(f"[ERROR] 操作失败: {str(e)}")

# ======================
# 脚本入口
# ======================

if __name__ == "__main__":
    # Step 1: 检查操作系统
    if os.name == 'nt':
        print("[INFO] 检测到Windows系统，开始执行绘制任务...")
        
        # Step 2: 执行主功能
        draw_square_in_paint()
        
        print("[INFO] 脚本执行完毕")
    else:
        print("[ERROR] 此脚本仅支持Windows系统")