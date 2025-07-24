from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox


class ListenerSettingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # 添加标题
        title_label = QLabel("其他设置")
        title_font = title_label.font()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # 添加print_commands开关
        self.print_commands_checkbox = QCheckBox("启用命令打印 (print_commands)")
        # 设置默认状态（例如默认不启用）
        self.print_commands_checkbox.setChecked(False)
        # 可以添加提示信息
        self.print_commands_checkbox.setToolTip("勾选后将打印执行的命令详情")
        layout.addWidget(self.print_commands_checkbox)

        # 添加伸缩项，使内容靠上显示
        layout.addStretch()