import time
from pynput import mouse
from typing import List, Dict, Tuple, Optional
import math
from transcriber.src.configs.drawer_panel_config import manager

# 存储拖拽事件的列表
mouse_records = []

# 当前拖拽的状态
current_drag = None

def on_move(x, y):
    """鼠标移动回调函数"""
    global current_drag
    if current_drag and current_drag['state'] == 'pressed':
        # 更新当前位置
        current_drag['current_position'] = (x, y)

        # 计算移动距离
        start_x, start_y = current_drag['start_position']
        distance = math.sqrt((x - start_x)**2 + (y - start_y)**2)

        # 如果移动距离超过阈值，则标记为拖拽
        if distance > 5:  # 5像素阈值
            current_drag['state'] = 'dragging'
            current_drag['start_time'] = time.time() - start_time
            # 添加第一个轨迹点
            timestamp = time.time() - start_time
            current_drag['path'].append({
                'time': f"{timestamp:.3f}s",
                'position': (int(x), int(y))
            })

def on_click(x, y, button, pressed):
    """鼠标点击回调函数"""
    global current_drag, start_time

    timestamp = time.time() - start_time

    if pressed:
        # 鼠标按下事件
        current_drag = {
            'state': 'pressed',
            'start_time': timestamp,
            'start_position': (int(x), int(y)),
            'button': str(button).split('.')[-1],
            'current_position': (int(x), int(y)),
            'end_time': None,
            'end_position': None,
            'path': [],  # 轨迹点列表
            'button_name': None
        }

        # 检查按下的按钮区域
        clicked_button = manager.find_button_at_point(x, y)
        if clicked_button:
            current_drag['button_name'] = clicked_button.name

            # 检查是否点击了结束按钮
            if clicked_button.name in ["WindowClose", "WindowMinimization"]:
                return False  # 停止监听器
    else:
        # 鼠标释放事件
        if current_drag:
            current_drag['end_time'] = timestamp
            current_drag['end_position'] = (int(x), int(y))

            # 如果拖拽中，添加最后一个轨迹点
            if current_drag['state'] == 'dragging':
                current_drag['path'].append({
                    'time': f"{timestamp:.3f}s",
                    'position': (int(x), int(y))
                })

            # 添加到拖拽事件列表
            mouse_records.append(current_drag)
            current_drag = None

    return True  # 继续监听

def print_record(drag_list: List[Dict]):
    """打印拖拽记录结果"""
    if not drag_list:
        print("未检测到任何拖拽事件")
        return

    print("\n拖拽记录结果：")
    print(f"{'序号':<4} | {'类型':<8} | {'持续时间':<8} | {'起点':<15} | {'终点':<15} | {'按钮区域':<20} | {'轨迹点数'}")
    print("-" * 85)

    for i, drag in enumerate(drag_list, 1):
        duration = drag['end_time'] - drag['start_time']
        start_pos = str(drag['start_position'])
        end_pos = str(drag['end_position'])
        button_name = drag.get('button_name', 'N/A')
        if button_name is None:
            button_name = 'N/A'
        path_points = len(drag['path'])

        drag_type = "点击" if drag['state'] == 'pressed' else "拖拽"

        print(f"{i:<4} | {drag_type:<8} | {duration:.3f}s | {start_pos:<15} | {end_pos:<15} | {button_name:<20} | {path_points}")

    print(f"\n共检测到 {len(drag_list)} 个事件")

def record_mouse(max_duration: int = 300):
    """
    记录鼠标拖拽，直到点击结束按钮或超时

    参数:
    max_duration: 最大记录时长(秒)，默认5分钟
    """
    global start_time, mouse_records, current_drag

    # 重置状态
    mouse_records = []
    current_drag = None

    start_time = time.time()

    print("开始记录鼠标拖拽...")
    print("点击 'WindowClose' 或 'WindowMinimization' 按钮结束记录")
    print(f"或等待 {max_duration} 秒自动结束")

    # 创建鼠标监听器
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click
    ) as listener:
        start_time = time.time()
        end_time = start_time + max_duration

        # 监听循环
        while listener.running:
            if time.time() > end_time:
                print("\n达到最大记录时长，停止记录")
                listener.stop()
                break
            time.sleep(0.1)  # 减少CPU占用

    return mouse_records