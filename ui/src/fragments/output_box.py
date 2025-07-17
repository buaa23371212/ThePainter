from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar, QTextEdit, QAction


class OutputDisplay(QWidget):
    """带工具栏的输出显示栏组件"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化输出显示栏及工具栏"""
        # 主布局（垂直排列：工具栏 + 文本显示区）
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 1. 创建工具栏
        self.toolbar = QToolBar()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文字在图标旁边
        self.init_toolbar_actions()
        main_layout.addWidget(self.toolbar)

        # 2. 创建文本显示区
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # 只读模式
        main_layout.addWidget(self.text_edit)

        # 初始状态设置
        self.setVisible(False)

    def init_toolbar_actions(self):
        """初始化工具栏按钮"""
        # 清空按钮
        self.clear_action = QAction("清空", self)
        # 如需图标可添加：QAction(QIcon("path/to/icon"), "清空", self)
        self.clear_action.setToolTip("清空输出内容")
        self.clear_action.triggered.connect(self.clear_content)
        self.toolbar.addAction(self.clear_action)

        # 显示/隐藏按钮
        self.toggle_action = QAction("隐藏", self)
        self.toggle_action.setToolTip("显示/隐藏输出栏")
        self.toggle_action.triggered.connect(self.toggle_visibility)
        self.toolbar.addAction(self.toggle_action)

        # 可选：添加复制按钮
        self.copy_action = QAction("复制", self)
        self.copy_action.setToolTip("复制选中内容")
        self.copy_action.triggered.connect(self.copy_content)
        self.toolbar.addAction(self.copy_action)

    # 工具栏功能实现
    def clear_content(self):
        """清空输出内容"""
        self.text_edit.clear()

    def toggle_visibility(self):
        """切换输出栏显示状态"""
        current_visible = self.isVisible()
        self.setVisible(not current_visible)
        self.toggle_action.setText("隐藏" if not current_visible else "显示")

    def copy_content(self):
        """复制选中内容到剪贴板"""
        self.text_edit.copy()

    # 对外提供的文本追加接口（保持原有使用方式兼容）
    def append(self, text):
        """追加文本内容"""
        self.text_edit.append(text)

    # 可选：其他常用接口封装
    def setText(self, text):
        """设置文本内容"""
        self.text_edit.setText(text)

    def text(self):
        """获取当前文本内容"""
        return self.text_edit.toPlainText()