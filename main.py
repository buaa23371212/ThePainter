import os
from tool.utils import open_paint
from parser.command_parser import parse_arguments
from drawer.circle_drawer import select_circle_tool, draw_circle_command
from drawer.rectangle_drawer import select_rectangle_tool, draw_rectangle_command
from drawer.polygon_drawer import select_polygon_tool, draw_polygon_command
from drawer.line_drawer import select_line_tool, draw_line_command
from terminal_logger.logger import info, warn, error

def execute_command(args):
    """
    执行绘图命令
    
    Step:
    1. 根据命令类型选择对应的绘图工具
    2. 调用相应的绘图函数执行绘图操作
    3. 捕获并处理可能发生的异常
    
    :param args: 解析后的命令行参数
    """
    try:
        # Step 1: 选择绘图工具
        if args.command == 'circle':
            select_circle_tool()
            # Step 2: 执行绘图命令
            draw_circle_command(args)

        elif args.command == 'rectangle':
            select_rectangle_tool()
            # Step 2: 执行绘图命令
            draw_rectangle_command(args)

        elif args.command == 'polygon':
            select_polygon_tool()
            # Step 2: 执行绘图命令
            draw_polygon_command(args)

        elif args.command == 'line':
            select_line_tool()
            # Step 2: 执行绘图命令
            draw_line_command(args)

        else:
            # Step 3: 处理不支持的命令
            warn(True, f"暂不支持的命令: {args.command}", True)
    except Exception as e:
        # Step 4: 捕获并记录异常
        error(True, f"操作失败: {str(e)}", True)

def main():
    """
    主程序入口
    
    Step:
    1. 解析命令行参数
    2. 检查是否提供了输入文件
    3. 打开画图工具
    4. 执行绘图命令（单命令或批量命令）
    5. 处理异常情况
    """
    # Step 1: 解析命令行参数
    args = parse_arguments()

    if args.input_file:
        try:
            # Step 2: 打开画图工具
            open_paint()
            
            # Step 3: 批量执行文件中的命令
            with open(args.input_file, 'r') as file:
                for line in file:
                    # 解析每行命令
                    command_args = line.strip().split()
                    parsed_args = parse_arguments(command_args)
                    # 执行命令
                    execute_command(parsed_args)
            
            # Step 4: 显示完成信息
            info(True, "画图工具保持打开状态", True)
        except Exception as e:
            # Step 5: 处理异常
            error(True, f"操作失败: {str(e)}", True)
    else:
        try:
            # Step 2: 打开画图工具
            open_paint()
            # Step 3: 执行单条命令
            execute_command(args)
            # Step 4: 显示完成信息
            info(True, "画图工具保持打开状态", True)
        except Exception as e:
            # Step 5: 处理异常
            error(True, f"操作失败: {str(e)}", True)

if __name__ == "__main__":
    """
    程序入口点
    
    Step:
    1. 检查操作系统类型
    2. 在Windows系统上执行主程序
    3. 在非Windows系统上显示错误
    """
    # Step 1: 检查操作系统
    if os.name == 'nt':
        info(True, "检测到Windows系统，开始执行绘制任务...", True)
        # Step 2: 执行主程序
        main()
        info(True, "脚本执行完毕", True)
    else:
        # Step 3: 非Windows系统提示
        error(True, "此脚本仅支持Windows系统", True)