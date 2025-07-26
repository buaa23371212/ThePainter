from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton

from src.main.python.utils.listener_manager import listener_config
from src.main.python.terminal_logger.logger import debug


class ListenerSettingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # 添加print_commands开关
        self.print_commands_checkbox = QCheckBox("启用命令打印 (print_commands)")

        # 设置默认状态（例如默认不启用）
        debug(True, repr(listener_config.DEFAULT_PRINT_STATE))
        self.print_commands_checkbox.setChecked(listener_config.DEFAULT_PRINT_STATE)
        
        self.print_commands_checkbox.stateChanged.connect(self.update_print_state)

        # 可以添加提示信息
        self.print_commands_checkbox.setToolTip("勾选后将打印执行的命令详情")
        layout.addWidget(self.print_commands_checkbox)

        # 添加确定按钮并连接保存事件
        self.confirm_button = QPushButton("确定")
        self.confirm_button.setFixedHeight(40)
        self.confirm_button.clicked.connect(self.save_settings)  # 连接点击事件
        layout.addWidget(self.confirm_button)

        # 添加伸缩项，使内容靠上显示
        layout.addStretch()

    def is_print_commands_enabled(self):
        """返回print_commands_checkbox的勾选状态"""
        return self.print_commands_checkbox.isChecked()
    
    def save_settings(self):
        listener_config.save_config()

    def update_print_state(self, state):
        """当勾选状态改变时，同步更新listener_config的DEFAULT_PRINT_STATE"""
        # state为2表示勾选，0表示未勾选（Qt的状态值定义）
        listener_config.DEFAULT_PRINT_STATE = "True" if state == 2 else "False"