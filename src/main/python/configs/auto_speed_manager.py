import re

from src.main.python.configs.project_config import auto_speed_config_path

class AutoSpeedConfig:
    _instance = None  # 单例模式确保配置唯一

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        """从配置文件加载配置项"""
        try:
            with open(auto_speed_config_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 提取配置值的正则表达式
            pattern = r"^(\w+)\s*=\s*(.+)$"
            configs = {}
            
            for line in content.split("\n"):
                match = re.match(pattern, line.strip())
                if match:
                    key, value = match.groups()
                    try:
                        # 尝试转换为数值类型
                        configs[key] = float(value) if '.' in value else int(value)
                    except ValueError:
                        configs[key] = value  # 保留原始字符串（如果转换失败）

            # 初始化配置属性
            self.MULTIPLIER_FACTOR = configs.get("MULTIPLIER_FACTOR", 1.0)
            self.BASIC_DRAW_DURATION_1 = configs.get("BASIC_DRAW_DURATION_1", 0.5)
            self.BASIC_DRAW_DURATION_2 = configs.get("BASIC_DRAW_DURATION_2", 0.3)
            self.BASIC_DRAW_DURATION_3 = configs.get("BASIC_DRAW_DURATION_3", 0.2)
            self.BASIC_CLICK_WAIT = configs.get("BASIC_CLICK_WAIT", 0.5)
            self.BASIC_MOUSE_MOVE_SPEED = configs.get("BASIC_MOUSE_MOVE_SPEED", 0.5)
            self.BASIC_EXTRA_MOVE_DELAY = configs.get("BASIC_EXTRA_MOVE_DELAY", 0.2)

            # 计算派生属性
            self.calculate_actual_values()

        except FileNotFoundError:
            # 文件不存在时使用默认值
            self._set_defaults()

    def _set_defaults(self):
        """设置默认配置"""
        self.MULTIPLIER_FACTOR = 1.0
        self.BASIC_DRAW_DURATION_1 = 0.5
        self.BASIC_DRAW_DURATION_2 = 0.3
        self.BASIC_DRAW_DURATION_3 = 0.2
        self.BASIC_CLICK_WAIT = 0.5
        self.BASIC_MOUSE_MOVE_SPEED = 0.5
        self.BASIC_EXTRA_MOVE_DELAY = 0.2
        self.calculate_actual_values()

    def calculate_actual_values(self):
        """计算实际使用的属性值"""
        self.ACTUAL_DRAW_DURATION_1 = self.BASIC_DRAW_DURATION_1 / self.MULTIPLIER_FACTOR
        self.ACTUAL_DRAW_DURATION_2 = self.BASIC_DRAW_DURATION_2 / self.MULTIPLIER_FACTOR
        self.ACTUAL_DRAW_DURATION_3 = self.BASIC_DRAW_DURATION_3 / self.MULTIPLIER_FACTOR
        self.ACTUAL_CLICK_WAIT = self.BASIC_CLICK_WAIT / self.MULTIPLIER_FACTOR
        self.ACTUAL_MOUSE_MOVE_SPEED = self.BASIC_MOUSE_MOVE_SPEED / self.MULTIPLIER_FACTOR
        self.ACTUAL_EXTRA_MOVE_DELAY = self.BASIC_EXTRA_MOVE_DELAY / self.MULTIPLIER_FACTOR
        self.ACTUAL_HALF_EXTRA_MOVE_DELAY = self.ACTUAL_EXTRA_MOVE_DELAY / 2

    def save_config(self):
        """将当前配置保存到文件"""
        # 读取原始文件内容（保留注释和格式）
        try:
            with open(auto_speed_config_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []

        # 需要更新的基础配置项（派生项不再保存，由类自动计算）
        base_configs = {
            "MULTIPLIER_FACTOR": self.MULTIPLIER_FACTOR,
            "BASIC_DRAW_DURATION_1": self.BASIC_DRAW_DURATION_1,
            "BASIC_DRAW_DURATION_2": self.BASIC_DRAW_DURATION_2,
            "BASIC_DRAW_DURATION_3": self.BASIC_DRAW_DURATION_3,
            "BASIC_CLICK_WAIT": self.BASIC_CLICK_WAIT,
            "BASIC_MOUSE_MOVE_SPEED": self.BASIC_MOUSE_MOVE_SPEED,
            "BASIC_EXTRA_MOVE_DELAY": self.BASIC_EXTRA_MOVE_DELAY
        }

        # 替换配置值，保留注释和格式
        new_lines = []
        for line in lines:
            stripped = line.strip()
            # 检查是否是配置行
            for key, value in base_configs.items():
                if stripped.startswith(f"{key} ="):
                    # 保留注释部分
                    if '#' in line:
                        prefix, comment = line.split('#', 1)
                        new_line = f"{key} = {value}  # {comment}"
                    else:
                        new_line = f"{key} = {value}\n"
                    new_lines.append(new_line)
                    break
            else:
                # 不是配置行，保留原样
                new_lines.append(line)

        # 如果文件不存在或配置项缺失，创建新内容
        if not new_lines:
            new_lines = [
                "# 自动操作相关速度配置\n",
                f"MULTIPLIER_FACTOR = {self.MULTIPLIER_FACTOR}\n",
                "\n",
                f"BASIC_DRAW_DURATION_1 = {self.BASIC_DRAW_DURATION_1}\n",
                f"BASIC_DRAW_DURATION_2 = {self.BASIC_DRAW_DURATION_2}\n",
                f"BASIC_DRAW_DURATION_3 = {self.BASIC_DRAW_DURATION_3}\n",
                f"BASIC_CLICK_WAIT = {self.BASIC_CLICK_WAIT}\n",
                f"BASIC_MOUSE_MOVE_SPEED = {self.BASIC_MOUSE_MOVE_SPEED}\n",
                f"BASIC_EXTRA_MOVE_DELAY = {self.BASIC_EXTRA_MOVE_DELAY}\n",
            ]

        # 写入更新后的内容
        with open(auto_speed_config_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    def toString(self):
        """返回配置信息的字符串表示"""
        config_str = [
            "AutoSpeedConfig 配置信息：",
            f"  倍率系数: {self.MULTIPLIER_FACTOR}",
            f"  基础绘制时长1: {self.BASIC_DRAW_DURATION_1}",
            f"  基础绘制时长2: {self.BASIC_DRAW_DURATION_2}",
            f"  基础绘制时长3: {self.BASIC_DRAW_DURATION_3}",
            f"  基础点击等待时间: {self.BASIC_CLICK_WAIT}",
            f"  基础鼠标移动速度: {self.BASIC_MOUSE_MOVE_SPEED}",
            f"  基础额外移动延迟: {self.BASIC_EXTRA_MOVE_DELAY}",
            "\n  计算后实际值：",
            f"  实际绘制时长1: {self.ACTUAL_DRAW_DURATION_1}",
            f"  实际绘制时长2: {self.ACTUAL_DRAW_DURATION_2}",
            f"  实际绘制时长3: {self.ACTUAL_DRAW_DURATION_3}",
            f"  实际点击等待时间: {self.ACTUAL_CLICK_WAIT}",
            f"  实际鼠标移动速度: {self.ACTUAL_MOUSE_MOVE_SPEED}",
            f"  实际额外移动延迟: {self.ACTUAL_EXTRA_MOVE_DELAY}",
            f"  实际半程额外移动延迟: {self.ACTUAL_HALF_EXTRA_MOVE_DELAY}"
        ]
        return "\n".join(config_str)


auto_speed_config = AutoSpeedConfig()
auto_speed_config.load_config()