import os

from tools.terminal_logger.logger import info

# 只显示 input 和 output 文件夹
DIR_FILTER = ["input","output"]

# 如果是命令文件，显示工具栏
# 支持多种命令文件类型
COMMAND_FILE_TYPES = ['.pcmd', '.cmd', '.txt']

# 图片后缀
IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]

# 各类文件目录，路径等配置

# 项目根目录
current_file_path = os.path.abspath(__file__)           # 获取当前文件的绝对路径
current_dir = os.path.dirname(current_file_path)        # 获取当前文件所在的目录: ./configs/ui_config
project_root = os.path.dirname(os.path.dirname(current_dir))

info(True, f"项目根目录: {project_root}", True)

# css
css_dir = os.path.join(project_root, "ui", "css")
info(True, f"css目录: {css_dir}", True)