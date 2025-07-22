import os

from src.main.python.terminal_logger.logger import info

def is_project_root_valid(proj_root):
    """
    验证项目根目录是否以'ThePainter'结尾

    Args:
        proj_root: 待验证的项目根目录路径

    Returns:
        bool: 若路径以'ThePainter'结尾则返回True，否则返回False
    """
    # 获取路径的最后一个组件（文件夹名称）
    last_component = os.path.basename(proj_root)
    return last_component == 'ThePainter'

current_file_path = os.path.abspath(__file__)                   # 获取当前文件的绝对路径
current_dir = os.path.dirname(current_file_path)                # 获取当前文件所在的目录: src/main/python/configs
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

info(True, f"项目根目录: {project_root}", True)

# work_dir = QDir.currentPath()
#
# info(True, f"当前工作目录: {work_dir}", True)

if is_project_root_valid(project_root):
    info(True, f"项目根目录验证通过: {project_root}", True)
else:
    info(True, f"项目根目录验证失败: {project_root} 不是以'ThePainter'结尾", True)

def get_project_root():
    return project_root

# painter.py
painter_dir = os.path.join(project_root, "src", "main", "python", "auto_drawer")

listener_dir = os.path.join(project_root, "src", "main", "python", "transcriber")

# CSS 文件目录
css_dir = os.path.join(project_root, "src", "main", "resources", "css")

input_dir = os.path.join(project_root, "src", "main", "resources", "input")
output_dir = os.path.join(project_root, "src", "main", "resources", "output")