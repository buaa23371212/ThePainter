from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
)

from public_utils.terminal_logger.logger import info
from ui.src.configs.ui_config import TITLE_HEIGHT


class ListenerPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 主布局：垂直布局（标题 + 分栏内容）
        self.output_view = None
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)
        main_layout.setContentsMargins(4, 4, 4, 4)          # 设置内边距

        # ==================================================
        # 标题栏
        # ==================================================
        title_label = QLabel("屏幕监听器")
        title_label.setFixedHeight(TITLE_HEIGHT)            # 固定高度
        title_label.setObjectName("listenerTitleLabel")     # 添加对象名
        main_layout.addWidget(title_label)

        # 创建右侧容器（垂直布局）
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # 工具栏（仅对命令文件显示）
        self.toolbar = QFrame()
        self.toolbar.setObjectName("explorerToolbar")   # 添加对象名

        toolbar_layout = QHBoxLayout(self.toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        toolbar_layout.setAlignment(Qt.AlignRight)

        # 执行按钮
        self.execute_btn = QPushButton("执行命令")
        self.execute_btn.setObjectName("executeButton")  # 添加对象名
        self.execute_btn.setVisible(False)
        self.execute_btn.clicked.connect(self.execute_commands)
        toolbar_layout.addWidget(self.execute_btn)

        # 显示输出栏按钮
        self.display_btn = QPushButton("显示输出")
        self.display_btn.setObjectName("displayButton")
        self.display_btn.clicked.connect(self.display_commands)
        toolbar_layout.addWidget(self.display_btn)

        right_layout.addWidget(self.toolbar)
        right_layout.addWidget(QWidget())

        main_layout.addWidget(right_container)

    def set_output_view(self, text_view):
        """设置命令执行输出的目标文本视图"""
        self.output_view = text_view

    def execute_commands(self):
        pass

    def display_commands(self):
        self.output_view.setVisible(True)
        info(True, "输出已显示", True)