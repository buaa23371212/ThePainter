import os
import pyautogui
import argparse
from drawer.utils import open_paint
from drawer.circle_drawer import select_circle_tool, draw_circle, draw_circle_by_center

# ======================
# 主功能方法（支持命令行参数）
# ======================

def main():
    """主函数：解析命令行参数并执行对应操作"""
    parser = argparse.ArgumentParser(description='在画图工具中绘制圆形')
    parser.add_argument('-circle', nargs=4, type=int, metavar=('start_x', 'start_y', 'end_x', 'end_y'),
                       help='通过起点和终点绘制圆形（四个整数坐标）')
    parser.add_argument('-circle_by_center', nargs=3, type=int, metavar=('center_x', 'center_y', 'radius'),
                       help='通过圆心和半径绘制圆形')
    
    args = parser.parse_args()

    try:
        # 打开画图工具并选择圆形工具
        open_paint()
        select_circle_tool()
        
        # 根据参数执行不同绘制方式
        if args.circle:
            start_x, start_y, end_x, end_y = args.circle
            draw_circle(start_x, start_y, end_x, end_y)
        elif args.circle_by_center:
            center_x, center_y, radius = args.circle_by_center
            draw_circle_by_center(center_x, center_y, radius)
        else:
            # 默认行为：在屏幕中心绘制圆
            screen_width, screen_height = pyautogui.size()
            center_x, center_y = screen_width // 2, screen_height // 2
            draw_circle_by_center(center_x, center_y, 100)
        
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