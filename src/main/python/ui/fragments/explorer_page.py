import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeWidget, QTextEdit,
    QSplitter, QStackedWidget
)

from src.main.python.configs import ui_config
from src.main.python.configs.project_config import input_dir, output_dir
from src.main.python.configs.ui_config import TITLE_HEIGHT
from src.main.python.terminal_logger.logger import info
from src.main.python.ui.fragments.tool_bar import PreviewToolbar
from src.main.python.ui.utils.command_generator import execute_command_file
from src.main.python.ui.utils.file_display import FileDisplayUtils
from src.main.python.ui.utils.file_tree_utils import FileTreeUtils
from src.main.python.ui.utils.style_loader import load_stylesheets


class FileExplorer(QWidget):
    """
    资源管理器面板，只显示 input 和 output 文件夹内容，右侧显示文件内容
    增加对命令文件(.pcmd)的特殊支持
    """
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
        title_label = QLabel("资源管理器")
        title_label.setFixedHeight(TITLE_HEIGHT)  # 固定高度
        title_label.setObjectName("explorerTitleLabel")  # 添加对象名用于样式定制
        main_layout.addWidget(title_label)

        # ====================================================================
        # STEP 3: 创建内容区分割器（左右分栏）
        # ====================================================================
        # 使用水平分割器实现可调整的左右分栏
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)  # 添加到主布局

        # ====================================================================
        # STEP 4: 创建左侧文件树组件
        # ====================================================================
        self.tree = QTreeWidget()  # 创建树形控件显示文件结构
        self.tree.setHeaderHidden(True)  # 隐藏表头
        self.tree.setColumnWidth(0, 250)  # 设置列宽
        splitter.addWidget(self.tree)  # 添加到分割器左侧

        # ====================================================================
        # STEP 5: 创建右侧预览区容器
        # ====================================================================
        # 创建右侧容器（垂直布局）
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # ====================================================================
        # STEP 5.1: 添加预览工具栏
        # ====================================================================
        self.toolbar = PreviewToolbar()  # 创建工具栏实例
        right_layout.addWidget(self.toolbar)  # 添加到右侧布局顶部

        # ====================================================================
        # STEP 5.2: 连接工具栏按钮信号
        # ====================================================================
        self.toolbar.execute_btn.clicked.connect(self.execute_commands)
        self.toolbar.refresh_btn.clicked.connect(self.refresh_commands)
        self.toolbar.display_btn.clicked.connect(self.display_commands)

        # ====================================================================
        # STEP 5.3: 创建预览区域（堆叠组件）
        # ====================================================================
        self.stack = QStackedWidget()  # 创建堆叠组件实现多类型预览

        # 文本预览视图
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        self.stack.addWidget(self.text_view)  # index 0 - 文本预览

        # 图片预览视图
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(self.image_view)  # index 1 - 图片预览

        right_layout.addWidget(self.stack)  # 添加到右侧布局
        self.stack.setCurrentIndex(0)  # 默认显示文本预览

        splitter.addWidget(right_container)  # 将右侧容器添加到分割器

        # ====================================================================
        # STEP 6: 初始化文件树结构
        # ====================================================================
        # 准备要显示的文件夹路径
        root_paths = [
            input_dir,
            output_dir
        ]

        # 使用工具类构建文件树
        FileTreeUtils.build_file_tree(
            self.tree,
            root_paths,
            folder_icon="folder_icon.png",
            file_icon="file_icon.png"
        )

        # ====================================================================
        # STEP 7: 连接文件树事件
        # ====================================================================
        self.tree.itemClicked.connect(self.on_item_clicked)

        # ====================================================================
        # STEP 8: 初始化状态变量
        # ====================================================================
        self.current_file_path = None  # 当前选中的文件路径

        # ====================================================================
        # STEP 9: 加载样式表（可选）
        # ====================================================================
        # self.load_stylesheet()

    # ========================================================================
    # 文件树事件处理模块
    # ========================================================================
    def on_item_clicked(self, item, column):
        """
        处理文件树节点点击事件
        :param item: 被点击的节点
        :param column: 列索引
        """
        # STEP 1: 获取节点存储的路径
        path = item.data(0, Qt.UserRole)
        self.current_file_path = path

        # STEP 2: 显示工具栏
        self.toolbar.setVisible(True)

        # STEP 3: 根据文件类型设置工具栏按钮状态
        if path and os.path.isfile(path) and any(path.endswith(ext) for ext in ui_config.COMMAND_FILE_TYPES):
            self.toolbar.execute_btn.setVisible(True)  # 命令文件显示执行按钮
        else:
            self.toolbar.execute_btn.setVisible(False)  # 其他文件隐藏执行按钮

        # STEP 4: 显示文件内容或清空预览区
        if path and os.path.isfile(path):
            # 调用工具类方法显示文件内容
            FileDisplayUtils.display_file_content(
                path,
                self.text_view,
                self.image_view,
                self.stack
            )
        else:
            # 点击文件夹时清空预览区
            self.text_view.clear()
            self.stack.setCurrentIndex(0)  # 切换到文本预览
            self.toolbar.setVisible(False)  # 隐藏工具栏

    # ========================================================================
    # 辅助功能模块
    # ========================================================================
    def load_stylesheet(self):
        """加载样式表（可选）"""
        load_stylesheets(self, "")

    def set_output_view(self, text_view):
        """设置命令执行输出的目标文本视图"""
        self.output_view = text_view

    # ========================================================================
    # 命令执行模块
    # ========================================================================
    def execute_commands(self):
        """执行命令文件，输出到指定的文本视图"""
        # 检查输出视图和当前文件是否有效
        if hasattr(self, 'output_view') and self.current_file_path:
            self.output_view.setVisible(True)                               # 显示输出视图
            execute_command_file(self.current_file_path, self.output_view)  # 执行命令
        else:
            # 输出错误信息
            info(False, "未设置输出视图或未选择命令文件", True)

    # ========================================================================
    # 预览操作模块
    # ========================================================================
    def refresh_commands(self):
        """刷新当前预览的文件内容"""
        # 调用工具类方法刷新显示
        FileDisplayUtils.display_file_content(
            self.current_file_path,
            self.text_view,
            self.image_view,
            self.stack
        )
        info(True, "文件显示已刷新", True)  # 输出成功信息

    def display_commands(self):
        """显示输出面板"""
        if self.output_view:
            self.output_view.setVisible(True)  # 显示输出面板
            info(True, "输出已显示", True)  # 输出成功信息