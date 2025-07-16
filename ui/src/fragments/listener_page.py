from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

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