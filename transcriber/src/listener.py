import os

from public_configs.project_config import get_project_root
from public_utils.terminal_logger.logger import info
from transcriber.src.utils.command_generator import convert_events_to_drawing_commands, print_command
from transcriber.src.utils.mouse_recorder import record_mouse, print_record, export_to_file

file_path = os.path.join(get_project_root(), "transcriber", "test", "resources", "json", "mouse_event.json")

if __name__ == "__main__":
    info(True, "建议提前启动画图工具并保持最小化状态")

    mouse_records = record_mouse()

    # print_record(mouse_records)

    # export_to_file(mouse_records, file_path)

    commands = convert_events_to_drawing_commands(mouse_records)

    print_command(commands)