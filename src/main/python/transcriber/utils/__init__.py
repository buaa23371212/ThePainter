# 默认文件路径
import os
from src.main.python.configs.project_config import json_dir, input_dir, test_json_dir


DEFAULT_FILE_PATH = os.path.join(
    test_json_dir,
    "mouse_event.json"
)

POLYGON_TOLERANCE = 5.0