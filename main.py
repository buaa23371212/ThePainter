import os
from tool.utils import open_paint
from parser.command_parser import parse_arguments
from drawer.circle_drawer import select_circle_tool, draw_circle_command
from drawer.square_drawer import select_rectangle_tool, draw_square_command
from terminal_logger.logger import info, warn, error

def execute_command(args):
    try:
        if args.command == 'circle':
            select_circle_tool()
            draw_circle_command(args)

        elif args.command == 'square':
            select_rectangle_tool()
            draw_square_command(args)

        else:
            warn(True, f"暂不支持的命令: {args.command}")
    except Exception as e:
        error(True, f"操作失败: {str(e)}")

def main():
    # 解析命令行参数
    args = parse_arguments()

    if args.input_file:
        try:
            open_paint()
            with open(args.input_file, 'r') as file:
                for line in file:
                    command_args = line.strip().split()
                    parsed_args = parse_arguments(command_args)
                    execute_command(parsed_args)
            info(True, "画图工具保持打开状态")
        except Exception as e:
            error(True, f"操作失败: {str(e)}")
    else:
        try:
            open_paint()
            execute_command(args)
            info(True, "画图工具保持打开状态")
        except Exception as e:
            error(True, f"操作失败: {str(e)}")

if __name__ == "__main__":
    if os.name == 'nt':
        info(True, "检测到Windows系统，开始执行绘制任务...")
        main()
        info(True, "脚本执行完毕")
    else:
        error(True, "此脚本仅支持Windows系统")