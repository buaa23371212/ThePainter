from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

from public_utils.terminal_logger.logger import info
from configs.ui_config import TITLE_HEIGHT
from ui.src.fragments.tool_bar import ListenerToolbar


class ListenerPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # ====================================================================
        # STEP 1: 初始化主布局和基本设置
        # ====================================================================
        self.output_view = None  # 输出视图引用
        main_layout = QVBoxLayout(self)  # 创建主垂直布局
        self.setLayout(main_layout)
        main_layout.setContentsMargins(4, 4, 4, 4)  # 设置内边距

        # ====================================================================
        # STEP 2: 创建标题栏
        # ====================================================================
        title_label = QLabel("屏幕监听器")
        title_label.setFixedHeight(TITLE_HEIGHT)  # 固定高度
        title_label.setObjectName("listenerTitleLabel")  # 添加对象名用于样式定制
        main_layout.addWidget(title_label)

        # ====================================================================
        # STEP 3: 创建主内容容器
        # ====================================================================
        # 创建右侧容器（垂直布局）
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # ====================================================================
        # STEP 4: 创建工具栏
        # ====================================================================
        # 创建监听器专用工具栏
        self.toolbar = ListenerToolbar()
        right_layout.addWidget(self.toolbar)  # 添加到布局顶部

        # ====================================================================
        # STEP 5: 连接工具栏按钮信号
        # ====================================================================
        self.toolbar.execute_btn.clicked.connect(self.execute_commands)
        self.toolbar.display_btn.clicked.connect(self.display_commands)

        # ====================================================================
        # STEP 6: 添加内容区占位组件
        # ====================================================================
        # 目前使用空组件占位，后续可添加实际内容
        right_layout.addWidget(QWidget())  # 添加一个空的占位组件

        # ====================================================================
        # STEP 7: 将主内容容器添加到主布局
        # ====================================================================
        main_layout.addWidget(right_container)

    # ========================================================================
    # 输出视图设置模块
    # ========================================================================
    def set_output_view(self, text_view):
        """设置命令执行输出的目标文本视图"""
        self.output_view = text_view

    # ========================================================================
    # 命令执行模块
    # ========================================================================
    def execute_commands(self):
        """
        执行监听器命令
        (待实现具体功能)
        """
        # 预留命令执行功能接口
        # 后续可在此处添加屏幕监听逻辑
        pass

    # ========================================================================
    # 输出显示模块
    # ========================================================================
    def display_commands(self):
        """显示输出面板"""
        if self.output_view:
            self.output_view.setVisible(True)  # 显示输出面板
            info(True, "输出已显示", True)  # 输出成功信息