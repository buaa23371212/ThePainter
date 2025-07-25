import os

from src.main.python.terminal_logger.logger import info, warn

# =============================================================================
# 项目根目录验证模块
# =============================================================================

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

# =============================================================================
# 项目路径计算模块
# =============================================================================

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)
# 获取当前文件所在目录 (src/main/python/configs)
current_dir = os.path.dirname(current_file_path)
# 计算项目根目录路径 (向上回溯4级目录)
project_root = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(current_dir)
        )
    )
)

# 打印项目根目录信息
info(True, f"项目根目录: {project_root}", True)

# 验证项目根目录有效性
if is_project_root_valid(project_root):
    info(True, f"项目根目录验证通过: {project_root}", True)
else:
    warn(True, f"项目根目录验证失败: {project_root} 不是以'ThePainter'结尾", True)

# =============================================================================
# 路径获取接口模块
# =============================================================================

def get_project_root():
    """返回计算得到的项目根目录路径"""
    return project_root

# =============================================================================
# 关键目录定义模块
# =============================================================================
# python 源代码目录
python_dir = os.path.join(project_root, 'src', 'main', 'python')

# resources 目录
resources_dir = os.path.join(project_root, 'src', 'main', 'resources')

# data 目录
data_dir = os.path.join(project_root, "data")

# 自动绘图模块目录
painter_dir = os.path.join(python_dir, "auto_drawer")

# 鼠标动作转录模块目录
listener_dir = os.path.join(python_dir, "transcriber")

# CSS资源目录
css_dir = os.path.join(resources_dir, "css")

# 输入/输出资源目录
input_dir = os.path.join(data_dir, "input")
output_dir = os.path.join(data_dir, "output")

# json 资源目录
json_dir = os.path.join(data_dir, "json")

# 测试用 json 资源目录
test_json_dir = os.path.join(project_root, "src", "test", "resources", "json")

# 配置文件目录
configs_dir = os.path.join(python_dir, "configs")

# 测试配置文件目录
test_configs_dir = os.path.join(project_root, "src", "test", "python", "configs")
# 测试用自动速度配置文件路径
test_auto_speed_config_path = os.path.join(test_configs_dir, "auto_speed_config.py")

def generate_input_path(path_frag):
    return os.path.join(input_dir, path_frag)