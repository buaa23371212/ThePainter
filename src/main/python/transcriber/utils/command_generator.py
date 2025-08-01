import os.path
from typing import List, Dict, Optional, Union

from src.main.python.transcriber.utils import POLYGON_TOLERANCE
from src.main.python.utils.file_manager import generate_input_path
from src.main.python.terminal_logger.logger import warn

# ======================================================================
# 模块1：全局状态管理
# ======================================================================
# Step 1.1：定义全局绘图状态变量
current_tool = "pen"                    # 当前选中的绘图工具（笔、形状等）
current_color = "black"                 # 当前选中的颜色
current_shape = None                    # 当前选中的形状工具类型（圆、矩形等）
current_shape_border = "solid"          # 形状边框样式
current_shape_fill = "solid"            # 形状填充样式
current_shape_thickness = 5             # 线条/描边粗细
current_font = "Microsoft YaHei UI"     # 当前字体
current_font_size = 11                  # 字体大小
current_pen = "brush"                   # 笔刷类型
current_layer = 1                       # 当前工作图层

# Step 1.2：图形选择跟踪状态
is_graphic_selected = False             # 标记是否有图形被选中

# Step 1.3：绘图位置跟踪
start_position = None                   # 当前绘图动作的起始位置
end_position = None                     # 当前绘图动作的结束位置
control_points = None


# ======================================================================
# 模块2：命令生成工具
# ======================================================================
def is_curve_completed(control_points: List[tuple]) -> bool:
    """判断曲线是否绘制完成（拥有两个控制点）"""
    return len(control_points) == 2


def is_polygon_completed(control_points: List[tuple], start_position: tuple, tolerance: float = POLYGON_TOLERANCE) -> bool:
    """
    判断多边形是否绘制完成（最后一个控制点与起始点距离小于阈值）
    
    参数:
        control_points: 控制点列表
        start_position: 起始点坐标
        tolerance: 距离阈值（默认使用全局常量）
    """
    if not control_points or not start_position:
        return False
        
    last_point = control_points[-1]
    # 计算欧氏距离
    dx = last_point[0] - start_position[0]
    dy = last_point[1] - start_position[1]
    distance = (dx**2 + dy**2) ** 0.5  # 开平方获取实际距离
    
    return distance < tolerance


def generate_shape_command() -> Optional[str]:
    """
    根据当前工具和位置生成绘图命令
    
    Step 2.1：处理形状工具
    - 支持圆形、椭圆、矩形：生成带边界框的命令
    - 支持直线：生成带端点坐标的命令
    
    返回值：
        str: 生成的命令字符串，不适用时返回None
    """
    if current_tool == "shape":
        # Step 2.1.1：处理闭合形状（圆/椭圆/矩形）
        if current_shape in ["circle", "ellipse", "square", "rectangle", "rounded_rectangle"]:
            x1, y1 = start_position
            x2, y2 = end_position
            return f"{current_shape} -bounding {x1} {y1} {x2} {y2}"

        # Step 2.1.2：处理直线
        if current_shape in ["line"] and start_position and end_position:
            x1, y1 = start_position
            x2, y2 = end_position
            return f"line -points {x1} {y1} {x2} {y2}"
        
        # Step 2.1.3：处理曲线
        if current_shape == 'curve':
            if control_points:
                if not is_curve_completed(control_points):
                    raise ValueError(f'曲线需要2个控制点，当前已添加{len(control_points)}个')
                x0, y0 = start_position
                x1, y1 = control_points[0]
                x2, y2 = control_points[1]
                x3, y3 = end_position
                return f"curve -points {x0} {y0} {x1} {y1} {x2} {y2} {x3} {y3}"
            else:
                raise ValueError('未记录控制点')

        # Step 2.1.4：处理多边形
        if current_shape == 'polygon':
            if control_points:
                last_point = control_points[-1]
                if not is_polygon_completed(control_points, start_position):
                    raise ValueError(f'多边形未闭合（最后一点与起点距离超过阈值）')
                x1, y1 = start_position
                x2, y2 = end_position
                vertices = [f"{x1} {y1}", f"{x2} {y2}"]
                for point in control_points[:-1]:
                    px, py = point
                    vertices.append(f"{px} {py}")
                return f"polygon -points {' '.join(vertices)}"
            else:
                raise ValueError('未记录控制点')

        return None
    return None


def generate_color_command():
    """生成颜色设置命令"""
    return f"-color {current_color}"

def generate_fill_command():
    """生成填充命令（使用当前颜色填充指定位置）"""
    x, y = start_position
    return f"fill -x {x} -y {y}"


# ======================================================================
# 模块3：事件到命令的转换
# ======================================================================
def convert_events_to_drawing_commands(event_list: List[Dict]) -> List[str]:
    """
    将鼠标事件转换为绘图命令
    
    Step 3.1：遍历所有鼠标事件
    - 处理按钮点击：工具选择/颜色选择/填充操作
    - 处理拖拽事件：图形绘制
    
    参数：
        event_list (List[Dict]): 记录的鼠标事件列表
        
    返回值：
        List[str]: 生成的绘图命令列表
    """
    global is_graphic_selected, start_position, end_position, control_points, current_shape, current_tool, current_color

    commands = []  # 存储生成的命令
    i = 0  # 事件索引

    # Step 3.1：遍历所有鼠标事件
    while i < len(event_list):
        event = event_list[i]
        event_type = event['state']  # 事件类型（按下/拖拽）
        button_name = event.get('button_name', 'N/A') or 'N/A'  # 关联的按钮名称

        # Step 3.2：处理按钮按下事件
        if event_type == 'pressed':
            # TODO: 硬编码写在init
            if button_name == "AddLayer":
                commands.append("add_layer")

            # Step 3.2.1：形状工具选择
            if button_name.startswith('Shape_'):
                if is_graphic_selected == True:
                    deselect_and_generate(commands)

                current_tool = 'shape'
                current_shape = button_name[len('Shape_'):]         # 提取形状类型

                if current_shape in ['curve', 'polygon']:
                    control_points = []

            # Step 3.2.2：颜色选择
            elif button_name.startswith('Color_'):
                if is_graphic_selected == True:
                    deselect_and_generate(commands)

                current_color = button_name[len('Color_'):]
                commands.append(generate_color_command())           # 生成颜色命令

            # Step 3.2.3：工具选择
            elif button_name.startswith('Tool_'):
                if is_graphic_selected == True:
                    deselect_and_generate(commands)

                current_tool = button_name[len('Tool_'):]

            # Step 3.2.4：图形控制点操作
            elif button_name == 'Canvas' and current_tool == 'shape' and is_graphic_selected == True:
                if current_shape == 'curve' and not is_curve_completed(control_points):
                    control_points.append(event['start_position'])

                elif current_shape == 'polygon' and not is_polygon_completed(control_points):
                    control_points.append(event['start_position'])

                else:
                    deselect_and_generate(commands)

            # Step 3.2.5：填充操作
            elif button_name == 'Canvas' and current_tool == 'fill':
                start_position = event['start_position']            # 获取填充位置
                commands.append(generate_fill_command())            # 生成填充命令

            # Step 3.2.6：取消图形选中状态
            elif (button_name == 'Canvas' or button_name == 'N/A') and is_graphic_selected == True:
                deselect_and_generate(commands)

        # Step 3.3：处理拖拽事件（图形绘制）
        if event_type == 'dragging':
            if is_graphic_selected == False:
                is_graphic_selected = True
                start_position = event['start_position']            # 记录起始位置
                end_position = event['end_position']                # 记录结束位置

            elif is_graphic_selected == True:
                if current_shape == 'curve':
                    if not is_curve_completed(control_points):
                        control_points.append(event['end_position'])  # 添加控制点

        i += 1                                                      # 处理下一个事件

    return commands

def deselect_and_generate(commands):
    global is_graphic_selected, control_points

    is_graphic_selected = False
    try:
        cmd = generate_shape_command()
    except Exception as e:
                    # 捕获所有异常，将异常信息格式化为注释命令
        cmd = f"# {e}"
    control_points = []
    if cmd:
        commands.append(cmd)  # 生成最终形状命令
    else:
        warn(True, '空指令生成', True)


# ======================================================================
# 模块：其他工具
# ======================================================================
def print_command(commands: List[str]):
    print("\nGenerated Drawing Commands:")
    for i, cmd in enumerate(commands, 1):
        print(f"{cmd}")

def export2pcmd(commands: List[str], folder: Union[str, None] = None) -> None:
    """
    将生成的绘图命令导出到.pcmd文件中
    
    参数:
        folder: 可选参数，文件夹路径（folder_path）或文件夹名称（folder_name）
                - 若为文件夹路径，直接使用该路径
                - 若为文件夹名称，在当前工作目录下创建/使用该文件夹
                - 若为None，使用默认路径（由generate_input_path决定）
        commands: 要写入文件的命令列表，每条命令为一个字符串
    
    说明:
        函数会自动创建目标文件夹（若不存在），并将命令按行写入commands.pcmd文件
    """
    # 处理文件夹路径
    if folder is not None:
        # 拼接文件夹与文件名
        file_name = "commands.pcmd"
        folder_path = folder  # 无论是路径还是名称，都直接用于拼接
        tar_path = generate_input_path(os.path.join(folder_path, file_name))
    else:
        # 若未提供folder，直接使用默认路径生成（仅包含文件名）
        tar_path = generate_input_path("commands.pcmd")
    
    # 确保目标目录存在
    os.makedirs(os.path.dirname(tar_path), exist_ok=True)
    
    # 将命令列表写入文件，每行一条命令
    with open(tar_path, 'w', encoding='utf-8') as f:
        for cmd in commands:
            f.write(f"{cmd}\n")