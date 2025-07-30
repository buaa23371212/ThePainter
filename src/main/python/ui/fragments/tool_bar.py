from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton


class PreviewToolbar(QFrame):
    """预览区域的工具栏，用于操作当前预览的文件"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("explorerToolbar")   # 添加对象名
        self.setVisible(False)                  # 默认隐藏

        # 创建工具栏布局
        toolbar_layout = QHBoxLayout(self)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        toolbar_layout.setAlignment(Qt.AlignRight)

        # 执行按钮
        self.execute_btn = QPushButton("执行命令")
        self.execute_btn.setObjectName("executeButton")
        self.execute_btn.setVisible(False)
        toolbar_layout.addWidget(self.execute_btn)

        # 刷新按钮
        self.refresh_btn = QPushButton("刷新")
        self.refresh_btn.setObjectName("refreshButton")
        toolbar_layout.addWidget(self.refresh_btn)

        # 显示输出栏按钮
        self.display_btn = QPushButton("显示输出")
        self.display_btn.setObjectName("displayButton")
        toolbar_layout.addWidget(self.display_btn)

class ListenerToolbar(QFrame):
    """<UNK>"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("listenerToolbar")

        # 创建工具栏布局
        toolbar_layout = QHBoxLayout(self)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        toolbar_layout.setAlignment(Qt.AlignRight)

        # 执行按钮
        self.execute_btn = QPushButton("开始")
        self.execute_btn.setObjectName("executeButton")  # 添加对象名
        toolbar_layout.addWidget(self.execute_btn)

        # 显示输出栏按钮
        self.display_btn = QPushButton("显示输出")
        self.display_btn.setObjectName("refreshButton")
        toolbar_layout.addWidget(self.display_btn)

        # 保存设置按钮
        self.save_btn = QPushButton("保存设置")
        self.save_btn.setObjectName("saveButton")
        toolbar_layout.addWidget(self.save_btn)