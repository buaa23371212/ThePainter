from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QListWidget,
    QListWidgetItem, QStackedWidget, QLabel, QDoubleSpinBox,
    QSlider, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt

from utils.terminal_logger.logger import info

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        # 设置页面主布局
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # ==================================================
        # 左侧设置类型列表
        # ==================================================
        self.settings_list = QListWidget()
        self.settings_list.setFixedWidth(150)

        # 添加设置类型
        settings_types = ["自动操作速度", "其他设置"]  # 可扩展更多设置类型
        for setting in settings_types:
            self.settings_list.addItem(QListWidgetItem(setting))

        main_layout.addWidget(self.settings_list)

        # ==================================================
        # 右侧具体设置区域（堆叠页面）
        # ==================================================
        self.settings_stack = QStackedWidget()

        # 页面1: 自动操作速度设置
        speed_page = QWidget()
        speed_layout = QVBoxLayout(speed_page)  # 改为垂直布局，以便在底部添加按钮

        # 表单布局用于放置设置项
        form_layout = QFormLayout()

        # 倍速因子设置
        form_layout.addRow(QLabel("倍速因子:"))
        self.multiplier_spin = QDoubleSpinBox()
        self.multiplier_spin.setRange(0.1, 5.0)
        self.multiplier_spin.setSingleStep(0.1)
        self.multiplier_spin.setValue(1.0)
        form_layout.addRow(self.multiplier_spin)

        # 基础绘图持续时间1
        form_layout.addRow(QLabel("基础绘图时间1 (秒):"))
        self.draw_duration1 = QDoubleSpinBox()
        self.draw_duration1.setRange(0.01, 2.0)
        self.draw_duration1.setSingleStep(0.05)
        self.draw_duration1.setValue(0.5)
        form_layout.addRow(self.draw_duration1)

        # 基础绘图持续时间2
        form_layout.addRow(QLabel("基础绘图时间2 (秒):"))
        self.draw_duration2 = QDoubleSpinBox()
        self.draw_duration2.setRange(0.01, 2.0)
        self.draw_duration2.setSingleStep(0.05)
        self.draw_duration2.setValue(0.3)
        form_layout.addRow(self.draw_duration2)

        # 基础绘图持续时间3
        form_layout.addRow(QLabel("基础绘图时间3 (秒):"))
        self.draw_duration3 = QDoubleSpinBox()
        self.draw_duration3.setRange(0.01, 2.0)
        self.draw_duration3.setSingleStep(0.05)
        self.draw_duration3.setValue(0.2)
        form_layout.addRow(self.draw_duration3)

        # 点击等待时间
        form_layout.addRow(QLabel("点击等待时间 (秒):"))
        self.click_wait = QDoubleSpinBox()
        self.click_wait.setRange(0.01, 2.0)
        self.click_wait.setSingleStep(0.05)
        self.click_wait.setValue(0.5)
        form_layout.addRow(self.click_wait)

        # 鼠标移动速度
        form_layout.addRow(QLabel("鼠标移动速度:"))
        self.mouse_speed_slider = QSlider(Qt.Horizontal)  # 明确设置为水平方向
        self.mouse_speed_slider.setRange(1, 10)
        self.mouse_speed_slider.setValue(5)
        form_layout.addRow(self.mouse_speed_slider)

        # 额外移动延迟
        form_layout.addRow(QLabel("额外移动延迟 (秒):"))
        self.extra_delay = QDoubleSpinBox()
        self.extra_delay.setRange(0.01, 1.0)
        self.extra_delay.setSingleStep(0.05)
        self.extra_delay.setValue(0.2)
        form_layout.addRow(self.extra_delay)

        # 将表单添加到垂直布局
        speed_layout.addLayout(form_layout)

        # 添加垂直弹簧，使按钮保持在底部
        speed_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 添加确定按钮
        self.confirm_button = QPushButton("确定")
        self.confirm_button.setFixedHeight(40)  # 设置按钮高度
        self.confirm_button.clicked.connect(self.save_settings)  # 连接点击事件
        speed_layout.addWidget(self.confirm_button)

        self.settings_stack.addWidget(speed_page)

        # 页面2: 其他设置（占位）
        other_page = QWidget()
        other_layout = QVBoxLayout(other_page)
        other_layout.addWidget(QLabel("其他设置页面"))

        # 同样添加确定按钮
        other_confirm_button = QPushButton("确定")
        other_confirm_button.setFixedHeight(40)
        other_confirm_button.clicked.connect(self.save_settings)
        other_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        other_layout.addWidget(other_confirm_button)

        self.settings_stack.addWidget(other_page)

        main_layout.addWidget(self.settings_stack)

        # 连接设置类型选择事件
        self.settings_list.currentRowChanged.connect(self.settings_stack.setCurrentIndex)
        self.settings_list.setCurrentRow(0)  # 默认选择第一项

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

        info(True, settings_output, True)