import tkinter as tk
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

from src.main.python.terminal_logger.logger import info, debug
from src.main.python.configs.ui_config import TITLE_HEIGHT
from src.main.python.ui.fragments.listener_setting import ListenerSettingsWidget
from src.main.python.ui.fragments.listener_setting_page import ListenerSettingPage
from src.main.python.ui.fragments.tool_bar import ListenerToolbar
from src.main.python.ui.utils.command_generator import execute_listening_command
from src.main.python.ui.utils.file_manager import FileManager


class ListenerPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setting_page = None
        # ====================================================================
        # STEP 1: 初始化主布局和基本设置
        # ====================================================================
        self.output_view = None  # 输出视图引用
        main_layout = QVBoxLayout(self)  # 创建主垂直布局
        self.setLayout(main_layout)
        main_layout.setContentsMargins(4, 4, 4, 4)  # 设置内边距

        self.tk_root = tk.Tk()
        self.tk_root.withdraw()  # 隐藏Tkinter窗口
        self.file_manager = FileManager(self.tk_root)

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
        # STEP 6: 创建参数设置区域
        # ====================================================================
        self.settings_widget = ListenerSettingsWidget(self.file_manager)
        right_layout.addWidget(self.settings_widget)

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
        """执行监听器命令"""
        if hasattr(self, 'output_view'):
            self.output_view.setVisible(True)                           # 显示输出视图
            # 可以通过self.settings_widget获取参数
            action = self.settings_widget.get_action()
            input_file = self.settings_widget.get_input_file()
            output_file = self.settings_widget.get_output_file()
            print_commands = self.setting_page.is_print_commands_enabled()
            # 执行命令时可以使用这些参数
            execute_listening_command(
                text_view=self.output_view,
                action=action,
                input_file=input_file,
                output_file=output_file,
                print_commands=print_commands,
            )
        else:
            # 输出错误信息
            info(False, "未设置输出视图", True)

    # ========================================================================
    # 输出显示模块
    # ========================================================================
    def display_commands(self):
        """显示输出面板"""
        if self.output_view:
            self.output_view.setVisible(True)  # 显示输出面板
            info(True, "输出已显示", True)  # 输出成功信息

    def set_setting_page(self, setting_page: ListenerSettingPage):
        self.setting_page = setting_page