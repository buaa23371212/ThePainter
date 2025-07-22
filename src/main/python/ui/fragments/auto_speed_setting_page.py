from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QDoubleSpinBox,
    QSlider, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from src.main.python.terminal_logger.logger import info


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

        # 鼠标移动速度
        form_layout.addRow(QLabel("鼠标移动速度:"))
        self.mouse_speed_slider = QSlider(Qt.Horizontal)
        self.mouse_speed_slider.setRange(1, 10)
        form_layout.addRow(self.mouse_speed_slider)

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

        # 添加确定按钮
        self.confirm_button = QPushButton("确定")
        self.confirm_button.setFixedHeight(40)
        main_layout.addWidget(self.confirm_button)

    def load_settings(self):
        """加载设置（使用固定值模拟）"""
        info(True, "加载自动操作速度设置中...", True)

        # 模拟从配置文件或数据库加载的固定值
        default_settings = {
            "MULTIPLIER_FACTOR": 1.5,
            "BASIC_DRAW_DURATION_1": 0.6,
            "BASIC_DRAW_DURATION_2": 0.4,
            "BASIC_DRAW_DURATION_3": 0.3,
            "BASIC_CLICK_WAIT": 0.6,
            "BASIC_MOUSE_MOVE_SPEED": 7,
            "BASIC_EXTRA_MOVE_DELAY": 0.3
        }

        # 将加载的设置应用到界面控件
        self.multiplier_spin.setValue(default_settings["MULTIPLIER_FACTOR"])
        self.draw_duration1.setValue(default_settings["BASIC_DRAW_DURATION_1"])
        self.draw_duration2.setValue(default_settings["BASIC_DRAW_DURATION_2"])
        self.draw_duration3.setValue(default_settings["BASIC_DRAW_DURATION_3"])
        self.click_wait.setValue(default_settings["BASIC_CLICK_WAIT"])
        self.mouse_speed_slider.setValue(default_settings["BASIC_MOUSE_MOVE_SPEED"])
        self.extra_delay.setValue(default_settings["BASIC_EXTRA_MOVE_DELAY"])

        info(True, "自动操作速度设置加载完成", True)

    def get_current_settings(self):
        """获取当前设置值"""
        return {
            "MULTIPLIER_FACTOR": self.multiplier_spin.value(),
            "BASIC_DRAW_DURATION_1": self.draw_duration1.value(),
            "BASIC_DRAW_DURATION_2": self.draw_duration2.value(),
            "BASIC_DRAW_DURATION_3": self.draw_duration3.value(),
            "BASIC_CLICK_WAIT": self.click_wait.value(),
            "BASIC_MOUSE_MOVE_SPEED": self.mouse_speed_slider.value(),
            "BASIC_EXTRA_MOVE_DELAY": self.extra_delay.value()
        }

    def save_settings(self):
        """保存设置并在终端输出信息"""
        info(True, "已修改设置", True)

        # 获取当前设置值（仅用于演示，实际应用中可能需要保存这些值）
        current_settings = {
            "MULTIPLIER_FACTOR": self.multiplier_spin.value(),
            "BASIC_DRAW_DURATION_1": self.draw_duration1.value(),
            "BASIC_DRAW_DURATION_2": self.draw_duration2.value(),
            "BASIC_DRAW_DURATION_3": self.draw_duration3.value(),
            "BASIC_CLICK_WAIT": self.click_wait.value(),
            "BASIC_MOUSE_MOVE_SPEED": self.mouse_speed_slider.value(),
            "BASIC_EXTRA_MOVE_DELAY": self.extra_delay.value()
        }

        # 打印设置值（可选）
        settings_output = "当前设置值:\n"
        for key, value in current_settings.items():
            settings_output += f"{key}: {value}\n"