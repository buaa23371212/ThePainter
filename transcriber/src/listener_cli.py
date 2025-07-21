import os
import argparse
from configs.project_config import get_project_root
from public_utils.terminal_logger.logger import info
from transcriber.src.utils.command_generator import convert_events_to_drawing_commands, print_command
from transcriber.src.utils.mouse_recorder import record_mouse, print_record, export_to_file, parse_from_file

# 默认文件路径
DEFAULT_FILE_PATH = os.path.join(
    get_project_root(),
    "transcriber",
    "test",
    "resources",
    "json",
    "mouse_event.json"
)

def main():
    parser = argparse.ArgumentParser(
        description="Mouse Event Recorder and Processor",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-a', '--action',
        choices=['record', 'export', 'convert', 'full', 'parse'],
        default='record',
        help="""
选择要执行的操作：
  record     : 记录并打印鼠标事件（默认）
  export     : 记录并导出到文件
  convert    : 记录并转换为绘图命令
  full       : 记录、转换并打印绘图命令
  parse      : 从文件解析并转换为绘图命令
        """
    )
    parser.add_argument(
        '-f', '--file',
        default=DEFAULT_FILE_PATH,
        help=f"指定输入/输出文件路径（默认：{DEFAULT_FILE_PATH}）"
    )
    parser.add_argument(
        '-p', '--print-commands',
        action='store_true',
        help="在转换后打印绘图命令（仅对convert/parse操作有效）"
    )

    args = parser.parse_args()

    # 操作1：默认行为（记录并打印）
    if args.action == 'record':
        mouse_records = record_mouse()
        print_record(mouse_records)

    # 操作2：记录并导出
    elif args.action == 'export':
        mouse_records = record_mouse()
        export_to_file(mouse_records, args.file)
        info(True, f"鼠标事件已导出到: {args.file}")

    # 操作3：记录并转换
    elif args.action == 'convert':
        mouse_records = record_mouse()
        commands = convert_events_to_drawing_commands(mouse_records)
        if args.print_commands:
            print_command(commands)

    # 操作4：记录、转换并打印
    elif args.action == 'full':
        mouse_records = record_mouse()
        commands = convert_events_to_drawing_commands(mouse_records)
        print_command(commands)

    # 操作5：从文件解析并转换
    elif args.action == 'parse':
        mouse_records = parse_from_file(args.file)
        commands = convert_events_to_drawing_commands(mouse_records)
        if args.print_commands:
            print_command(commands)

if __name__ == "__main__":
    main()