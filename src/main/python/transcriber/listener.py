import os
import argparse

from src.main.python.configs.project_config import json_dir, input_dir, test_json_dir

from src.main.python.terminal_logger.logger import info, error
from src.main.python.transcriber import ACTION_CHOICE

from src.main.python.transcriber.utils.command_generator import convert_events_to_drawing_commands, print_command, \
    export2pcmd
from src.main.python.transcriber.utils.mouse_recorder import record_mouse, print_record, export2json, parse_from_file

# 默认文件路径
DEFAULT_FILE_PATH = os.path.join(
    test_json_dir,
    "mouse_event.json"
)

def main():
    parser = argparse.ArgumentParser(
        description="Mouse Event Recorder and Processor",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-a', '--action',
        choices=ACTION_CHOICE,
        default='record',
        help="""
选择要执行的操作：
  record          : 记录并打印鼠标事件（默认）
  export          : 记录并导出到文件
  convert         : 记录并转换为绘图命令
  full            : 记录、转换并打印绘图命令
  parse           : 从文件解析并转换为绘图命令
  parse_and_save  : 从文件解析、转换并保存绘图命令
        """
    )
    parser.add_argument(
        '-f', '--file',
        default=DEFAULT_FILE_PATH,
        help=f"指定鼠标事件输入/输出文件路径（默认：{DEFAULT_FILE_PATH}）"
    )
    parser.add_argument(
        '-c', '--command-file',
        help="指定绘图命令输出文件路径（仅对parse_and_save操作有效）"
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
        export2json(mouse_records, args.file)
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

    # 操作6：从文件解析、转换并保存（使用pass占位）
    elif args.action == 'parse_and_save':
        mouse_records = parse_from_file(args.file)
        commands = convert_events_to_drawing_commands(mouse_records)

        # 保存命令的功能占位符
        if args.command_file:
            export2pcmd(args.command_file, commands)
        else:
            error(True, "错误：未指定绘图命令输出文件路径（使用-c参数）")

if __name__ == "__main__":
    main()