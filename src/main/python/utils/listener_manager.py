import os
from src.main.python.configs.project_config import configs_dir
from src.main.python.utils.config_loader import parse_config_file, replace_lines
from src.main.python.terminal_logger.logger import debug

class ListenerConfig:
    _instance = None
    listener_config_path = os.path.join(configs_dir, "listener_config.py")

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
        self.DEFAULT_PRINT_STATE = configs.get("DEFAULT_PRINT_STATE", "False")
        self.DEFAULT_JSON_NAME = configs.get("DEFAULT_JSON_NAME", "mouse_event.json")
        self.DEFAULT_PCMD_NAME = configs.get("DEFAULT_PCMD_NAME", "commands.pcmd")
    
    def _set_defaults(self):
        """设置默认配置"""
        self.DEFAULT_ACTION_CHOICE = "record"
        self.DEFAULT_PRINT_STATE = "False"
        self.DEFAULT_JSON_NAME = "mouse_event.json"
        self.DEFAULT_PCMD_NAME = "commands.pcmd"

    def save_config(self):
        """将当前配置保存到文件"""
        try:
            with open(self.listener_config_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []

        base_configs = {
            "DEFAULT_ACTION_CHOICE": self.DEFAULT_ACTION_CHOICE,
            "DEFAULT_PRINT_STATE": self.DEFAULT_PRINT_STATE,
            "DEFAULT_JSON_NAME": self.DEFAULT_JSON_NAME,
            "DEFAULT_PCMD_NAME": self.DEFAULT_PCMD_NAME
        }

        new_lines = replace_lines(lines, base_configs)

        # 如果文件不存在或配置项缺失，创建新内容
        if not new_lines:
            new_lines = [
                f"DEFAULT_ACTION_CHOICE = {self.DEFAULT_ACTION_CHOICE}\n",
                "\n",
                f"DEFAULT_PRINT_STATE = {self.DEFAULT_PRINT_STATE}\n",
                "\n",
                f"DEFAULT_JSON_NAME = {self.DEFAULT_JSON_NAME}\n",
                f"DEFAULT_PCMD_NAME = {self.DEFAULT_PCMD_NAME}\n"
            ]

        # 写入更新后的内容
        with open(self.listener_config_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    def __str__(self):
        """返回对象的字符串表示"""
        return (f"\nListenerConfig(\n"
                f"  DEFAULT_ACTION_CHOICE: {self.DEFAULT_ACTION_CHOICE}\n"
                f"  DEFAULT_PRINT_STATE: {self.DEFAULT_PRINT_STATE}\n"
                f"  DEFAULT_JSON_NAME: {self.DEFAULT_JSON_NAME}\n"
                f"  DEFAULT_PCMD_NAME: {self.DEFAULT_PCMD_NAME}\n"
                f")")

listener_config = ListenerConfig()
debug(True, listener_config)