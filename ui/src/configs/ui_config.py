import os

from public_utils.terminal_logger.logger import info

# =====================================================
# 目录过滤器配置
# =====================================================
# 资源管理器只显示以下文件夹
DIR_FILTER = ["input", "output"]

# =====================================================
# 文件类型配置
# =====================================================
# 命令文件后缀类型（显示执行按钮）
COMMAND_FILE_TYPES = ['.pcmd', '.cmd', '.txt']

# 图片文件后缀类型（在预览区显示图片）
IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]

# =====================================================
# 路径配置
# =====================================================
# 项目根目录计算
current_file_path = os.path.abspath(__file__)                   # 获取当前文件的绝对路径
current_dir = os.path.dirname(current_file_path)                # 获取当前文件所在的目录: ./configs/ui_config
project_root = os.path.dirname(
    os.path.dirname(
        os.path.dirname(current_dir)
    ))                                                          # 项目根目录（上3级目录）

# 记录项目根目录（调试信息）
info(True, f"项目根目录: {project_root}", True)

# painter.py
painter_dir = os.path.join(project_root, "auto_drawer", "src")

# =====================================================
# 样式表配置
# =====================================================
# CSS 文件目录
css_dir = os.path.join(project_root, "ui", "src", "resources", "css")               # ./ui/css
info(True, f"CSS 目录: {css_dir}", True)