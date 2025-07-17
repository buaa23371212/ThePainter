import os
from PyQt5.QtCore import QDir

from public_utils.terminal_logger.logger import info

current_file_path = os.path.abspath(__file__)                   # 获取当前文件的绝对路径
current_dir = os.path.dirname(current_file_path)                # 获取当前文件所在的目录: ./public_configs
project_root = os.path.dirname(current_dir)

info(True, f"项目根目录: {project_root}", True)

# work_dir = QDir.currentPath()
#
# info(True, f"当前工作目录: {work_dir}", True)

def get_project_root():
    return project_root

input_dir = os.path.join(project_root, "input")
output_dir = os.path.join(project_root, "output")