import os
import pyautogui
from parser.command_parser import parse_arguments
from drawer.utils import open_paint
from drawer.circle_drawer import select_circle_tool, draw_circle_command
from drawer.square_drawer import select_rectangle_tool, draw_square_command

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
            print(f"[WARNING] 暂不支持的命令: {args.command}")
        
        print("[INFO] 画图工具保持打开状态")
    except Exception as e:
        print(f"[ERROR] 操作失败: {str(e)}")

# ======================
# 脚本入口
# ======================

if __name__ == "__main__":
    if os.name == 'nt':
        print("[INFO] 检测到Windows系统，开始执行绘制任务...")
        main()
        print("[INFO] 脚本执行完毕")
    else:
        print("[ERROR] 此脚本仅支持Windows系统")