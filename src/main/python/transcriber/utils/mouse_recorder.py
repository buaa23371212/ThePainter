# mouse_recorder.py
import json
import os
import time
from pynput import mouse
from typing import List, Dict
import math

from src.main.python.terminal_logger.logger import info, error
from src.main.python.configs.bottons_config import manager

# ======================================================================
# Module 1: Global Variables Initialization
# ======================================================================
# Stores all recorded mouse events
mouse_events = []

# Tracks the current in-progress mouse event
current_event = None

# ======================================================================
# Module 2: Mouse Movement Handling
# ======================================================================
def on_move(x, y):
    """Handles mouse movement events"""
    global current_event
    if current_event and current_event['state'] == 'pressed':
        # Update current position
        current_event['current_position'] = (x, y)

        # Calculate movement distance from start point
        start_x, start_y = current_event['start_position']
        distance = math.sqrt((x - start_x)**2 + (y - start_y)**2)

        # Check if movement exceeds drag threshold
        if distance > 5:  # 5-pixel threshold
            # Transition to dragging state
            current_event['state'] = 'dragging'
            current_event['start_time'] = time.time() - start_time

            # Record first path point
            timestamp = time.time() - start_time
            current_event['path'].append({
                'time': f"{timestamp:.3f}s",
                'position': (int(x), int(y))
            })

# ======================================================================
# Module 3: Mouse Click Handling
# ======================================================================
def on_click(x, y, button, pressed):
    """Handles mouse click events"""
    global current_event, start_time

    timestamp = time.time() - start_time

    # Step 3.1: Handle mouse press event
    if pressed:
        # Initialize new event record
        current_event = {
            'state': 'pressed',
            'start_time': timestamp,
            'start_position': (int(x), int(y)),
            'button': str(button).split('.')[-1],
            'current_position': (int(x), int(y)),
            'end_time': None,
            'end_position': None,
            'path': [],  # Stores movement path
            'button_name': None
        }

        # Step 3.2: Check if button area was clicked
        clicked_button = manager.find_button_at_point(x, y)
        if clicked_button:
            current_event['button_name'] = clicked_button.name

            # Step 3.3: Handle special termination buttons
            if clicked_button.name in ["WindowClose", "WindowMinimization"]:
                return False  # Stop listener

    # Step 3.4: Handle mouse release event
    elif current_event:
        # Finalize event record
        current_event['end_time'] = timestamp
        current_event['end_position'] = (int(x), int(y))

        # Add final point if dragging occurred
        if current_event['state'] == 'dragging':
            current_event['path'].append({
                'time': f"{timestamp:.3f}s",
                'position': (int(x), int(y))
            })

        # Store completed event
        mouse_events.append(current_event)
        current_event = None

    return True  # Continue listening

# ======================================================================
# Module 4: Event Reporting
# ======================================================================
def print_record(event_list: List[Dict]):
    """Prints recorded mouse events in formatted table"""
    # Step 4.1: Handle empty record case
    if not event_list:
        info(True, "未检测到任何鼠标事件")
        return

    # Step 4.2: Print table header
    print("\n鼠标事件记录：")
    print(f"{'序号':<4} | {'类型':<8} | {'持续时间':<8} | {'起点':<15} | {'终点':<15} | {'按钮区域':<20} | {'轨迹点数'}")
    print("-" * 85)

    # Step 4.3: Print each event record
    for i, event in enumerate(event_list, 1):
        duration = event['end_time'] - event['start_time']
        start_pos = str(event['start_position'])
        end_pos = str(event['end_position'])
        button_name = event.get('button_name', 'N/A')
        if button_name is None:
            button_name = 'N/A'
        path_points = len(event['path'])

        # Determine event type (click or drag)
        event_type = "点击" if event['state'] == 'pressed' else "拖拽"

        print(f"{i:<4} | {event_type:<8} | {duration:.3f}s | {start_pos:<15} | {end_pos:<15} | {button_name:<20} | {path_points}")

    # Step 4.4: Print summary
    print(f"\n共检测到 {len(event_list)} 个事件")

def export_to_file(event_list: List[Dict], file_path: str) -> None:
    """将事件列表导出到JSON文件"""
    try:
        # 创建目录（如果不存在）
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            # 确保中文等特殊字符正确编码
            json.dump(event_list, f, ensure_ascii=False, indent=4)
        info(True, f"成功导出到文件: {file_path}")
    except Exception as e:
        error(True, f"导出文件失败: {str(e)}")

def parse_from_file(file_path: str) -> List[Dict]:
    """从JSON文件解析出事件列表"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            event_list = json.load(f)
        # 验证解析结果是否为列表且元素为字典
        if isinstance(event_list, list) and all(isinstance(item, dict) for item in event_list):
            info(True, f"成功从文件解析: {file_path}")
            return event_list
        else:
            raise ValueError("文件内容格式不符合要求，应为列表且元素为字典")
    except FileNotFoundError:
        error(True, f"文件不存在: {file_path}")
        return []
    except Exception as e:
        error(True, f"解析文件失败: {str(e)}")
        return []


# ======================================================================
# Module 5: Main Recording Function
# ======================================================================
def record_mouse(max_duration: int = 300):
    """
    Records mouse events until termination button click or timeout

    Parameters:
    max_duration: Maximum recording time in seconds (default: 300)
    """
    global start_time, mouse_events, current_event

    # Step 5.1: Initialize recording state
    mouse_events = []
    current_event = None
    start_time = time.time()

    # Step 5.2: Start message
    info(True, "开始记录鼠标事件...")
    info(True, "点击 'WindowClose' 或 'WindowMinimization' 按钮结束记录")
    info(True, f"或等待 {max_duration} 秒自动结束")

    # Step 5.3: Create mouse listener
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click
    ) as listener:
        start_time = time.time()
        end_time = start_time + max_duration

        # Step 5.4: Main recording loop
        while listener.running:
            if time.time() > end_time:
                info(True, "\n达到最大记录时长，停止记录")
                listener.stop()
                break
            time.sleep(0.1)  # Reduce CPU usage

    return mouse_events