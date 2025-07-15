import os

from public_configs.project_config import get_project_root
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
project_root = get_project_root()

# painter.py
painter_dir = os.path.join(project_root, "auto_drawer", "src")

# =====================================================
# 样式表配置
# =====================================================
# CSS 文件目录
css_dir = os.path.join(project_root, "ui", "src", "resources", "css")               # ./ui/css
info(True, f"CSS 目录: {css_dir}", True)