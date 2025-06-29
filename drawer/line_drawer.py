import time
import pyautogui
from tool.utils import click_shapes_button, activate_canvas
from terminal_logger.logger import info

# ======================
# 专用功能方法
# ======================
def select_line_tool():
    """
    在画图工具中选择直线工具
    """
    # 使用info函数记录日志，但show=False不显示输出
    info(False, "选择直线工具...", True)
    
    # Step 1: 点击形状按钮
    click_shapes_button()
    
    # Step 2: 选择直线工具
    # presses=0
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    info(False, "已选择直线工具", True)
    
    # Step 3: 激活画布
    activate_canvas()

def draw_line(start_x, start_y, end_x, end_y):
    """
    在画图工具中绘制直线
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        end_x (int): 结束点X坐标
        end_y (int): 结束点Y坐标
    """
    # 使用info函数记录日志，但show=False不显示输出
    info(False, f"开始绘制直线 (起点: ({start_x}, {start_y}), 终点: ({end_x}, {end_y}))", True)
    
    # Step 1: 缓慢移动到起始位置
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    time.sleep(0.2)  # 额外延迟确保识别
    
    # Step 2: 按住Shift键绘制直线
    pyautogui.keyDown('shift')
    pyautogui.dragTo(end_x, end_y, duration=0.5)
    pyautogui.keyUp('shift')
    
    info(False, "成功绘制直线！", True)

def draw_line_by_vector(start_x, start_y, dx, dy):
    """
    通过起点和方向向量绘制直线
    
    参数:
        start_x (int): 起始点X坐标
        start_y (int): 起始点Y坐标
        dx (int): X方向向量
        dy (int): Y方向向量
    """
    end_x = start_x + dx
    end_y = start_y + dy
    draw_line(start_x, start_y, end_x, end_y)

# ======================
# 导出函数供主程序调用
# ======================
def draw_line_command(args):
    """
    执行绘制直线的命令
    
    参数:
        args: 解析后的命令行参数
    """
    if args.points:
        # 使用起点和终点坐标绘制直线
        start_x, start_y, end_x, end_y = args.points
        draw_line(start_x, start_y, end_x, end_y)
    elif args.vector:
        # 使用起点和方向向量绘制直线
        start_x, start_y, dx, dy = args.vector
        draw_line_by_vector(start_x, start_y, dx, dy)
    else:
        draw_line(500, 500, 600, 600)  # 默认绘制一条直线