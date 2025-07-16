from typing import List, Dict, Tuple, Optional

from transcriber.src.listener import file_path
from transcriber.src.utils.mouse_recorder import parse_from_file, print_record

# ======================================================================
# Module 1: Global State Management
# ======================================================================
# Step 1.1: Define global drawing state variables
current_tool = "pen"                    # Currently selected drawing tool
current_color = "black"                 # Currently selected color
current_shape = None                    # Currently selected shape tool
current_shape_border = "solid"          # Shape border style
current_shape_fill = "solid"            # Shape fill style
current_shape_thickness = 5             # Line/stroke thickness
current_font = "Microsoft YaHei UI"     # Current font
current_font_size = 11                  # Font size
current_pen = "brush"                   # Pen/brush type
current_layer = 1                       # Current working layer

# Step 1.2: Graphic selection tracking
is_graphic_selected = False             # Tracks if a graphic is currently selected

# Step 1.3: Drawing position tracking
start_position = None                   # Start position of current drawing action
end_position = None                     # End position of current drawing action


# ======================================================================
# Module 2: Command Generation Utilities
# ======================================================================
def generate_command() -> Optional[str]:
    """
    Generates drawing command based on current tool and positions

    Returns:
        str: Generated command string or None if not applicable
    """
    # Step 2.1: Handle shape tools
    if current_tool == "shape":
        if current_shape in ["circle", "ellipse", "rectangle"]:
            x1, y1 = start_position
            x2, y2 = end_position
            return f"{current_shape} -bounding {x1} {y1} {x2} {y2}"
        if current_shape in ["line"] and start_position and end_position:
            x1, y1 = start_position
            x2, y2 = end_position
            return f"line -points {x1} {y1} {x2} {y2}"

    # Step 2.2: Handle fill command
    elif current_tool == "fill" and start_position:
        x, y = start_position
        return f"fill -color {current_color} -x {x} -y {y}"

def generate_color_command():
    return f"-color {current_color}"


# ======================================================================
# Module 3: Event to Command Conversion
# ======================================================================
def convert_events_to_drawing_commands(event_list: List[Dict]) -> List[str]:
    """
    Converts mouse events into drawing commands

    Parameters:
        event_list (List[Dict]): List of recorded mouse events

    Returns:
        List[str]: Generated drawing commands
    """
    global is_graphic_selected, start_position, end_position, current_shape, current_tool

    commands = []
    i = 0

    # Step 3.1: Iterate through all mouse events
    while i < len(event_list):
        event = event_list[i]

        event_type = event['state']
        button_name = event.get('button_name', 'N/A') or 'N/A'

        if event_type == 'pressed':
            # 点击选择形状工具
            if button_name.startswith('Shape_'):
                pass

            # 点击选择颜色
            if button_name.startswith('Color_'):
                pass

            # 点击选择工具
            if button_name.startswith('Tool_'):
                pass

            # 点击取消上一个形状选中
            if button_name == 'Canvas' or button_name == 'N/A' and is_graphic_selected == True:
                pass

            # 点击填充颜色
            if current_tool == 'fill' and button_name == 'Canvas':
                pass

        if event_type == 'dragging':
            start_position = event['start_position']
            end_position = event['end_position']

        i += 1

    return commands

# ======================================================================
# Module 4: Main Execution
# ======================================================================
if __name__ == "__main__":
    # Step 4.1: Parse recorded mouse events
    mouse_events = parse_from_file(file_path)

    # Step 4.2: Print event records for debugging
    print_record(mouse_events)

    # Step 4.3: Convert events to drawing commands
    # drawing_commands = convert_events_to_drawing_commands(mouse_events)
    #
    # # Step 4.4: Print generated commands
    # print("\nGenerated Drawing Commands:")
    # for i, cmd in enumerate(drawing_commands, 1):
    #     print(f"{i:>2}. {cmd}")