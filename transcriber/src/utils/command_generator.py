from typing import List, Dict, Tuple, Optional

from public_utils.terminal_logger.logger import warn
from transcriber.src.listener import file_path
from transcriber.src.utils.mouse_recorder import parse_from_file, print_record

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


# ======================================================================
# 模块2：命令生成工具
# ======================================================================
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
    global is_graphic_selected, start_position, end_position, current_shape, current_tool, current_color

    commands = []  # 存储生成的命令
    i = 0  # 事件索引

    # Step 3.1：遍历所有鼠标事件
    while i < len(event_list):
        event = event_list[i]
        event_type = event['state']  # 事件类型（按下/拖拽）
        button_name = event.get('button_name', 'N/A') or 'N/A'  # 关联的按钮名称

        # Step 3.2：处理按钮按下事件
        if event_type == 'pressed':
            # Step 3.2.1：形状工具选择
            if button_name.startswith('Shape_'):
                current_tool = 'shape'
                current_shape = button_name[len('Shape_'):]  # 提取形状类型

            # Step 3.2.2：颜色选择
            elif button_name.startswith('Color_'):
                current_color = button_name[len('Color_'):]
                commands.append(generate_color_command())  # 生成颜色命令

            # Step 3.2.3：工具选择
            elif button_name.startswith('Tool_'):
                current_tool = button_name[len('Tool_'):]

            # TODO: Step 3.2.5：图形控制点操作
            elif button_name == 'Canvas' and current_tool == 'shape':
                pass

            # Step 3.2.5：填充操作
            elif button_name == 'Canvas' and current_tool == 'fill':
                start_position = event['start_position']  # 获取填充位置
                commands.append(generate_fill_command())  # 生成填充命令

            # Step 3.2.6：取消图形选中状态
            elif (button_name == 'Canvas' or button_name == 'N/A') and is_graphic_selected == True:
                is_graphic_selected = False
                cmd = generate_shape_command()
                if cmd:
                    commands.append(cmd)  # 生成最终形状命令
                else:
                    warn(True, 'line127', True)

        # Step 3.3：处理拖拽事件（图形绘制）
        if event_type == 'dragging':
            is_graphic_selected = True
            start_position = event['start_position']  # 记录起始位置
            end_position = event['end_position']      # 记录结束位置

        i += 1  # 处理下一个事件

    return commands


# ======================================================================
# 模块：其他工具
# ======================================================================
def print_command(commands: List[str]):
    print("\nGenerated Drawing Commands:")
    for i, cmd in enumerate(commands, 1):
        print(f"{i:>2}. {cmd}")


# ======================================================================
# 模块4：主执行流程
# ======================================================================
if __name__ == "__main__":
    # Step 4.1：从文件解析记录的鼠标事件
    mouse_events = parse_from_file(file_path)

    # Step 4.2：打印事件记录（调试用）
    print_record(mouse_events)

    # Step 4.3：将事件转换为绘图命令
    drawing_commands = convert_events_to_drawing_commands(mouse_events)

    # Step 4.4：打印生成的命令
    print_command(drawing_commands)