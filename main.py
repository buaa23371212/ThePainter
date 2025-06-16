import os
from drawer.utils import open_paint
from parser.command_parser import parse_arguments
from drawer.circle_drawer import select_circle_tool, draw_circle_command
from drawer.square_drawer import select_rectangle_tool, draw_square_command
from terminal_logger.logger import info, warn, error

# ======================
# 主功能方法（支持命令行参数）
# ======================

def main():
    """主函数：解析命令行参数并执行对应操作"""
    args = parse_arguments()  # 解析命令行参数

    try:
        # 打开画图工具并选择圆形工具
        open_paint()
        
        # 根据参数执行不同绘制方式
        if args.command == 'circle':
            select_circle_tool()
            draw_circle_command(args)
            
        elif args.command == 'square':
            select_rectangle_tool()
            draw_square_command(args)

        else:
            warn(True, f"暂不支持的命令: {args.command}", "main.py")
        
        info(True, "画图工具保持打开状态")
    except Exception as e:
        error(True, f"操作失败: {str(e)}", "main.py")

# ======================
# 脚本入口
# ======================

if __name__ == "__main__":
    if os.name == 'nt':
        info(True, "检测到Windows系统，开始执行绘制任务...")
        main()
        info(True, "脚本执行完毕")
    else:
        error(True, "此脚本仅支持Windows系统", "main.py")