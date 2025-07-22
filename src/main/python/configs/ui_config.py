import os

from src.main.python.configs.project_config import get_project_root
from src.main.python.terminal_logger.logger import info

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

TITLE_HEIGHT = 40