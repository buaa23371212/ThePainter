import time
import json
import pyautogui

from utils.tools.tools import activate_canvas, click_shapes_button
from utils.config.drawer_panel_config import get_shape_panel_presses
from utils.config import auto_speed_config

from terminal_logger.logger import info, error

# ======================
# 专用功能方法
# ======================

def select_polygon_tool():
    """
    在画图工具中选择多边形工具
    """
    info(False, "选择多边形工具...", True)
    
    # Step 1: 点击形状按钮
    click_shapes_button()

    # Step 2: 选择多边形工具
    pyautogui.press('right', presses=get_shape_panel_presses("polygon"))  # 按右方向键5次选择多边形工具
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    pyautogui.press('enter')
    time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)
    info(False, "已选择多边形工具", True)


def draw_polygon(points):
    """
    在画图工具中绘制多边形
    
    参数:
        points (list of tuple): 多边形顶点列表，每个顶点为 (x, y) 坐标元组
    """
    if len(points) < 3:
        info(True, "至少需要三个点来绘制多边形", True)
        return
    
    info(False, f"开始绘制多边形，顶点数: {len(points)}", True)
    activate_canvas()
    
    # Step 1: 缓慢移动到第一个顶点
    start_x, start_y = points[0]
    pyautogui.moveTo(start_x, start_y, duration=auto_speed_config.ACTUAL_MOUSE_MOVE_SPEED)
    time.sleep(auto_speed_config.ACTUAL_EXTRA_MOVE_DELAY)  # 额外延迟确保识别
    
    # Step 2: 绘制第一条边（从第一个顶点到第二个顶点）
    # 在第一个顶点按下鼠标
    pyautogui.mouseDown()
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    # 拖动到第二个顶点
    second_x, second_y = points[1]
    pyautogui.dragTo(second_x, second_y, duration=auto_speed_config.BASIC_DRAW_DURATION_2)
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    # 释放鼠标（完成第一条边）
    pyautogui.mouseUp()
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    # Step 3: 绘制后续顶点（从第三个顶点开始）
    for i in range(2, len(points)):
        # 移动到下一个顶点
        x, y = points[i]
        pyautogui.moveTo(x, y, duration=auto_speed_config.BASIC_DRAW_DURATION_3)
        time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
        
        # 点击添加顶点（自动连接到上一个点）
        pyautogui.click()
        time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    # Step 4: 闭合多边形（回到第一个顶点）
    pyautogui.moveTo(start_x, start_y, duration=auto_speed_config.BASIC_DRAW_DURATION_2)
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    # 点击闭合多边形
    pyautogui.click()
    time.sleep(auto_speed_config.ACTUAL_HALF_EXTRA_MOVE_DELAY)
    
    info(False, "成功绘制多边形！", True)

# ======================
# 多边形数据处理方法
# ======================

def load_polygon_from_json(file_path, polygon_id=None, polygon_name=None):
    """
    从JSON文件加载多边形顶点数据
    
    Step:
    1. 打开并读取JSON文件
    2. 解析JSON数据
    3. 根据ID或名称查找多边形
    4. 返回顶点列表
    
    参数:
        file_path (str): JSON文件路径
        polygon_id (str): 多边形的ID标识符
        polygon_name (str): 多边形的名称
    
    返回:
        list: 多边形顶点列表 [(x1, y1), (x2, y2), ...]
    """
    try:
        # Step 1: 打开文件
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Step 2: 获取多边形数据
        polygons = data.get('polygons', {})
        
        # Step 3: 根据ID或名称查找
        if polygon_id and polygon_id in polygons:
            return polygons[polygon_id].get('vertices', [])
        
        if polygon_name:
            for poly_id, poly_data in polygons.items():
                if poly_data.get('name') == polygon_name:
                    return poly_data.get('vertices', [])
        
        # 未找到多边形
        raise ValueError(f"在文件 {file_path} 中未找到指定多边形: id={polygon_id}, name={polygon_name}")
    
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON文件未找到: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"无效的JSON格式: {file_path}")

def convert_vertices_to_points(vertices):
    """
    将顶点整数列表转换为点元组列表
    
    Step:
    1. 验证顶点数量（必须是偶数）
    2. 每两个整数组成一个点
    3. 返回点元组列表
    
    参数:
        vertices (list of int): 顶点坐标列表 [x1, y1, x2, y2, ...]
    
    返回:
        list: 点元组列表 [(x1, y1), (x2, y2), ...]
    """
    # Step 1: 验证顶点数量
    if len(vertices) % 2 != 0:
        raise ValueError("顶点坐标数量必须为偶数")
    
    # Step 2: 转换格式
    points = []
    for i in range(0, len(vertices), 2):
        x = vertices[i]
        y = vertices[i+1]
        points.append((x, y))
    
    return points

# ======================
# 参数验证
# ======================

def validate_polygon_args(args):
    """
    验证多边形参数的有效性
    
    Step:
    1. 验证文件方式参数
    2. 验证顶点方式参数
    3. 确保参数组合有效
    
    参数:
        args: 命令行参数对象
    """
    # Step 1: 验证文件方式参数
    if args.file:
        if not (args.id or args.name):
            raise ValueError("使用文件时，必须提供-id或-name参数")
        if args.id and args.name:
            raise ValueError("不能同时使用-id和-name参数")
    
    # Step 2: 验证顶点方式参数
    elif args.vertices:
        if len(args.vertices) % 2 != 0:
            raise ValueError("顶点坐标数量必须为偶数")
        if len(args.vertices) < 6:
            raise ValueError("多边形至少需要3个顶点（6个坐标值）")
        if args.id or args.name:
            raise ValueError("直接指定顶点时，不能使用-id或-name参数")

# ======================
# 导出函数供主程序调用
# ======================

def draw_polygon_command(args):
    """
    处理多边形绘制命令
    
    Step:
    1. 验证参数有效性
    2. 获取多边形顶点数据
    3. 选择多边形工具
    4. 绘制多边形
    5. 处理异常
    
    参数:
        args: 命令行参数对象
    """
    try:
        # Step 1: 验证参数
        validate_polygon_args(args)
        
        points = []
        
        # Step 2: 获取顶点数据
        if args.file:
            # 从JSON文件加载多边形
            points = load_polygon_from_json(args.file, args.id, args.name)
        elif args.vertices:
            # 转换顶点列表为点元组
            points = convert_vertices_to_points(args.vertices)
        
        # 确保有足够的点
        if len(points) < 3:
            raise ValueError("多边形至少需要三个顶点")
        
        # Step 3: 绘制多边形
        draw_polygon(points)
        
    except Exception as e:
        error(True, f"绘制多边形失败: {str(e)}", True)