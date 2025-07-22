from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QDoubleSpinBox,
    QSlider, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from src.main.python.terminal_logger.logger import info
from src.main.python.configs.config_manager import auto_speed_config


class AutoOperationSpeedPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_settings()

    def init_ui(self):
        """初始化界面布局和控件"""
        # 主布局使用垂直布局，方便在底部添加按钮
        main_layout = QVBoxLayout(self)

        # 表单布局用于放置设置项
        form_layout = QFormLayout()

        # 倍速因子设置
        form_layout.addRow(QLabel("倍速因子:"))
        self.multiplier_spin = QDoubleSpinBox()
        self.multiplier_spin.setRange(0.1, 5.0)
        self.multiplier_spin.setSingleStep(0.1)
        form_layout.addRow(self.multiplier_spin)

        # 基础绘图持续时间1
        form_layout.addRow(QLabel("基础绘图时间1 (秒):"))
        self.draw_duration1 = QDoubleSpinBox()
        self.draw_duration1.setRange(0.01, 2.0)
        self.draw_duration1.setSingleStep(0.05)
        form_layout.addRow(self.draw_duration1)

        # 基础绘图持续时间2
        form_layout.addRow(QLabel("基础绘图时间2 (秒):"))
        self.draw_duration2 = QDoubleSpinBox()
        self.draw_duration2.setRange(0.01, 2.0)
        self.draw_duration2.setSingleStep(0.05)
        form_layout.addRow(self.draw_duration2)

        # 基础绘图持续时间3
        form_layout.addRow(QLabel("基础绘图时间3 (秒):"))
        self.draw_duration3 = QDoubleSpinBox()
        self.draw_duration3.setRange(0.01, 2.0)
        self.draw_duration3.setSingleStep(0.05)
        form_layout.addRow(self.draw_duration3)

        # 点击等待时间
        form_layout.addRow(QLabel("点击等待时间 (秒):"))
        self.click_wait = QDoubleSpinBox()
        self.click_wait.setRange(0.01, 2.0)
        self.click_wait.setSingleStep(0.05)
        form_layout.addRow(self.click_wait)

        # 鼠标移动时间
        form_layout.addRow(QLabel("鼠标移动时间 (秒):"))
        self.mouse_move_time = QDoubleSpinBox()
        self.mouse_move_time.setRange(0.01, 2.0)
        self.mouse_move_time.setSingleStep(0.05)
        form_layout.addRow(self.mouse_move_time)

        # 额外移动延迟
        form_layout.addRow(QLabel("额外移动延迟 (秒):"))
        self.extra_delay = QDoubleSpinBox()
        self.extra_delay.setRange(0.01, 1.0)
        self.extra_delay.setSingleStep(0.05)
        form_layout.addRow(self.extra_delay)

        # 将表单添加到主布局
        main_layout.addLayout(form_layout)

        # 添加垂直弹簧，使按钮保持在底部
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 添加确定按钮并连接保存事件
        self.confirm_button = QPushButton("确定")
        self.confirm_button.setFixedHeight(40)
        self.confirm_button.clicked.connect(self.save_settings)  # 连接点击事件
        main_layout.addWidget(self.confirm_button)

    def load_settings(self):
        """从配置管理器加载真实设置"""
        info(True, "加载自动操作速度设置中...", True)
        
        # 从配置管理器加载设置
        self.multiplier_spin.setValue(auto_speed_config.MULTIPLIER_FACTOR)
        self.draw_duration1.setValue(auto_speed_config.BASIC_DRAW_DURATION_1)
        self.draw_duration2.setValue(auto_speed_config.BASIC_DRAW_DURATION_2)
        self.draw_duration3.setValue(auto_speed_config.BASIC_DRAW_DURATION_3)
        self.click_wait.setValue(auto_speed_config.BASIC_CLICK_WAIT)
        self.mouse_move_time.setValue(auto_speed_config.BASIC_MOUSE_MOVE_SPEED)
        self.extra_delay.setValue(auto_speed_config.BASIC_EXTRA_MOVE_DELAY)

        info(True, "自动操作速度设置加载完成", True)

    def get_current_settings(self):
        """获取当前设置值"""
        return {
            "MULTIPLIER_FACTOR": self.multiplier_spin.value(),
            "BASIC_DRAW_DURATION_1": self.draw_duration1.value(),
            "BASIC_DRAW_DURATION_2": self.draw_duration2.value(),
            "BASIC_DRAW_DURATION_3": self.draw_duration3.value(),
            "BASIC_CLICK_WAIT": self.click_wait.value(),
            "BASIC_MOUSE_MOVE_SPEED": self.mouse_move_time.value(),
            "BASIC_EXTRA_MOVE_DELAY": self.extra_delay.value()
        }

    def save_settings(self):
        """保存设置到配置文件"""
        info(True, "正在保存自动操作速度设置...", True)
        
        # 获取当前界面设置
        current_settings = self.get_current_settings()
        
        # 更新配置管理器的值
        auto_speed_config.MULTIPLIER_FACTOR = current_settings["MULTIPLIER_FACTOR"]
        auto_speed_config.BASIC_DRAW_DURATION_1 = current_settings["BASIC_DRAW_DURATION_1"]
        auto_speed_config.BASIC_DRAW_DURATION_2 = current_settings["BASIC_DRAW_DURATION_2"]
        auto_speed_config.BASIC_DRAW_DURATION_3 = current_settings["BASIC_DRAW_DURATION_3"]
        auto_speed_config.BASIC_CLICK_WAIT = current_settings["BASIC_CLICK_WAIT"]
        auto_speed_config.BASIC_MOUSE_MOVE_SPEED = current_settings["BASIC_MOUSE_MOVE_SPEED"]
        auto_speed_config.BASIC_EXTRA_MOVE_DELAY = current_settings["BASIC_EXTRA_MOVE_DELAY"]
        
        # 保存到配置文件
        auto_speed_config.save_config()
        
        # 重新计算实际值
        auto_speed_config.calculate_actual_values()
        
        info(True, "自动操作速度设置已保存", True)
        info(True, auto_speed_config.toString(), True)  # 打印配置信息