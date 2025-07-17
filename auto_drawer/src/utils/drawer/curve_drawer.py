import time
import pyautogui

from auto_drawer.src.utils.data_processor import load_shape_from_json, convert_points_to_coords, validate_shape_args
from auto_drawer.src.utils.canvas_tools import click_shapes_button, activate_canvas
from configs import auto_speed_config
from configs.drawer_panel_config import get_shape_panel_presses

from auto_drawer.src.utils.drawer.line_drawer import draw_line

from public_utils.terminal_logger.logger import info, error

# ======================
# 专用功能方法
# ======================

def draw_curve(points):
    """
    在画图工具中绘制三次贝塞尔曲线

    前置条件
    - 确保已验证参数合法性
    
    参数:
        points (list of tuple): 曲线控制点列表，包含4个点 (起点, 控制点1, 控制点2, 终点)
    """
    info(False, f"开始绘制贝塞尔曲线: 起点={points[0]}, 终点={points[3]}", True)
    activate_canvas()
    
    # Step 1:
    start_x, start_y = points[0]
    end_x, end_y = points[3]
    draw_line(start_x, start_y, end_x, end_y)
    
    # Step 2: 调整第一个控制点
    ctrl1_x, ctrl1_y = points[1]
    pyautogui.moveTo(ctrl1_x, ctrl1_y, duration=auto_speed_config.BASIC_DRAW_DURATION_2)
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    pyautogui.click()
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    # Step 3: 调整第二个控制点
    ctrl2_x, ctrl2_y = points[2]
    pyautogui.moveTo(ctrl2_x, ctrl2_y, duration=auto_speed_config.BASIC_DRAW_DURATION_2)
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    pyautogui.click()
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    info(False, "成功绘制贝塞尔曲线！", True)

# ======================
# 曲线数据处理方法
# ======================

def load_curve_from_json(file_path, curve_id=None, curve_name=None):
    """
    从JSON文件加载曲线点数据
    
    Step:
    
    参数:
        file_path (str): JSON文件路径
        curve_id (str): 曲线的ID标识符
        curve_name (str): 曲线的名称
    
    返回:
        list: 曲线点列表 [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
    """
    return load_shape_from_json(file_path, "curves", curve_id, curve_name)

# ======================
# 参数验证
# ======================
def validate_point_count(points):
    if points:
        if len(points) != 4:
            raise ValueError("曲线需要8个坐标值（4个点）")

def validate_curve_args(args):
    """
    验证曲线参数的有效性
    
    Step:
    
    参数:
        args: 命令行参数对象
    """
    validate_shape_args(args)


# ======================
# 导出函数供主程序调用
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
    pyautogui.press('right', presses=get_shape_panel_presses("curve"))
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    pyautogui.press('enter')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    info(False, "已选择曲线工具", True)

def draw_curve_command(args):
    """
    处理曲线绘制命令
    
    Step:
    1. 验证参数有效性
    2. 获取曲线点数据
    3. 选择曲线工具
    4. 绘制曲线
    5. 处理异常
    
    参数:
        args: 命令行参数对象
    """
    try:
        # Step 1: 验证参数
        validate_curve_args(args)
        
        points = []
        
        # Step 2: 获取点数据
        if args.file:
            # 从JSON文件加载曲线
            points = load_curve_from_json(args.file, args.id, args.name)
        elif args.points:
            # 转换点列表为坐标元组
            points = convert_points_to_coords(args.points)

        validate_point_count(points)

        # Step 3: 绘制曲线
        draw_curve(points)
        
    except Exception as e:
        error(True, f"绘制曲线失败: {str(e)}", True)