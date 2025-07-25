import os
from src.main.python.configs.project_config import configs_dir
from src.main.python.utils.config_loader import parse_config_file, replace_lines

class ListenerConfig:
    _instance = None
    listener_config_path = os.path.join(configs_dir, "lietener_config.py")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_config()
        return cls._instance
    
    def load_config(self):
        """从配置文件加载配置项"""
        configs = parse_config_file(self.listener_config_path)

        if not configs:  # 如果配置为空（文件不存在或解析失败）
            self._set_defaults()
            return
        
        # 初始化配置属性
        self.DEFAULT_ACTION_CHOICE = configs.get("DEFAULT_ACTION_CHOICE", "record")
        self.DEFAULT_PRINT_STATE = configs.get("DEFAULT_PRINT_STATE", False)
    
    def _set_defaults(self):
        """设置默认配置"""
        self.DEFAULT_ACTION_CHOICE = "record"
        self.DEFAULT_PRINT_STATE = False

    def save_config(self):
        """将当前配置保存到文件"""
        try:
            with open(self.auto_speed_config_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []

        base_configs = {
            "DEFAULT_ACTION_CHOICE": self.DEFAULT_ACTION_CHOICE,
            "DEFAULT_PRINT_STATE": self.DEFAULT_PRINT_STATE
        }

        new_lines = replace_lines(lines, base_configs)

        # 如果文件不存在或配置项缺失，创建新内容
        if not new_lines:
            new_lines = [
                f"DEFAULT_ACTION_CHOICE = {self.DEFAULT_ACTION_CHOICE}\n",
                "\n",
                f"DEFAULT_PRINT_STATE = {self.DEFAULT_PRINT_STATE}\n",
            ]

        # 写入更新后的内容
        with open(self.listener_config_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

listener_config = ListenerConfig()