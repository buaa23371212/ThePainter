import os
from typing import Optional

from src.main.python.configs.project_config import input_dir


def generate_input_path(path_frag: Optional[str] = None) -> str:
    """
    生成完整的输入文件路径，支持不同场景的路径拼接
    
    参数:
        path_frag: 路径片段，可以是文件名、文件夹名或完整路径
                   - 若为None，返回默认输入目录路径
                   - 若为相对路径，拼接至默认输入目录
                   - 若为绝对路径，直接返回该路径（优先使用用户指定的绝对路径）
    
    返回值:
        str: 生成的完整路径
    """
    if path_frag is None:
        return input_dir
    
    # 检查是否为绝对路径（跨平台兼容）
    if os.path.isabs(path_frag):
        return path_frag
    
    # 相对路径则拼接至默认输入目录
    return os.path.join(input_dir, path_frag)