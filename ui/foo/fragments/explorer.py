import os

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QTextEdit,
    QSplitter, QStackedWidget, QPushButton, QHBoxLayout, QFrame
)

from ui.foo.configs import ui_config

from utils.terminal_logger.logger import info
from ui.foo.utils.command_generator import execute_command_file
from ui.foo.utils.style_loader import load_stylesheets


class FileExplorer(QWidget):
    """
    资源管理器面板，只显示 input 和 output 文件夹内容，右侧显示文件内容
    增加对命令文件(.pcmd)的特殊支持
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # 主布局：垂直布局（标题 + 分栏内容）
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)
        main_layout.setContentsMargins(4, 4, 4, 4)  # 设置内边距
        
        # ==================================================
        # 标题栏
        # ==================================================
        title_label = QLabel("资源管理器")
        title_label.setFixedHeight(28)  # 固定高度
        title_label.setObjectName("explorerTitleLabel")  # 添加对象名
        main_layout.addWidget(title_label)
        
        # ===================================================
        # 内容区：左右分栏布局
        # ===================================================
        # 使用水平分割器实现可调整的左右分栏
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)         # 添加到主布局

        # =====================================================
        # 左侧：文件树组件
        # =====================================================
        self.tree = QTreeWidget()               # 创建树形控件显示文件结构
        self.tree.setHeaderHidden(True)         # 隐藏表头
        self.tree.setColumnWidth(0, 250)        # 设置列宽
        splitter.addWidget(self.tree)           # 添加到分割器左侧
        
        # =====================================================
        # 右侧：文件内容预览组件
        # =====================================================
        # 创建右侧容器（垂直布局）
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        
        # 工具栏（仅对命令文件显示）
        self.toolbar = QFrame()
        self.toolbar.setFixedHeight(40)
        self.toolbar.setObjectName("explorerToolbar")   # 添加对象名
        self.toolbar.setVisible(False)                  # 默认隐藏
        
        toolbar_layout = QHBoxLayout(self.toolbar)
        toolbar_layout.setAlignment(Qt.AlignRight)
        
        # 执行按钮
        self.execute_btn = QPushButton("执行命令")
        self.execute_btn.setFixedSize(100, 30)
        self.execute_btn.setObjectName("executeButton")  # 添加对象名
        self.execute_btn.setVisible(False)
        self.execute_btn.clicked.connect(self.execute_commands)
        toolbar_layout.addWidget(self.execute_btn)

        # 刷新按钮
        self.refresh_btn = QPushButton("刷新")
        self.refresh_btn.setFixedSize(100, 30)
        self.refresh_btn.setObjectName("refreshButton")
        self.refresh_btn.clicked.connect(self.refresh_commands)
        toolbar_layout.addWidget(self.refresh_btn)
        
        right_layout.addWidget(self.toolbar)
        
        # 预览区域
        self.stack = QStackedWidget()
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(self.text_view)            # index 0
        self.stack.addWidget(self.image_view)           # index 1
        right_layout.addWidget(self.stack)
        self.stack.setCurrentIndex(0)
        
        splitter.addWidget(right_container)             # 添加到分割器右侧

        # =====================================================
        # 初始化文件树结构
        # =====================================================
        # 只显示 input 和 output 文件夹
        for folder in ui_config.DIR_FILTER:
            folder_path = os.path.join(QDir.currentPath(), folder)
            if os.path.exists(folder_path):
                # 创建顶级文件夹项
                folder_item = QTreeWidgetItem([folder])
                self.tree.addTopLevelItem(folder_item)  # 添加到树形控件
                # 递归添加子文件和子文件夹
                self._add_children(folder_item, folder_path)

        # 绑定树形控件的点击事件
        self.tree.itemClicked.connect(self.on_item_clicked)
        
        # 当前选中的文件路径
        self.current_file_path = None
        
        # 最后加载样式表
        self.load_stylesheet()

    def _add_children(self, parent_item, folder_path):
        """
        递归添加子文件和子文件夹到树形控件
        :param parent_item: 父节点
        :param folder_path: 当前文件夹路径
        """
        for name in os.listdir(folder_path):
            path = os.path.join(folder_path, name)
            child_item = QTreeWidgetItem([name])    # 创建子节点
            
            # 存储完整路径到用户数据
            child_item.setData(0, Qt.UserRole, path)
            
            parent_item.addChild(child_item)        # 添加到父节点
            
            # 如果是文件夹，递归添加其内容
            if os.path.isdir(path):
                self._add_children(child_item, path)

    def on_item_clicked(self, item, column):
        """
        处理文件树节点点击事件
        :param item: 被点击的节点
        :param column: 列索引
        """
        # 获取存储在节点中的路径
        path = item.data(0, Qt.UserRole)
        self.current_file_path = path

        self.toolbar.setVisible(True)

        # 如果是命令文件，显示工具栏
        if path and os.path.isfile(path) and any(path.endswith(ext) for ext in ui_config.COMMAND_FILE_TYPES):
            self.execute_btn.setVisible(True)
        else:
            self.execute_btn.setVisible(False)

        # 显示文件内容或清空预览区
        if path and os.path.isfile(path):
            self.display_file_content(path)
        else:
            # 点击的是文件夹时清空预览区
            self.text_view.clear()
            self.stack.setCurrentIndex(0)
            self.toolbar.setVisible(False)


    def display_file_content(self, path):
        """
        根据文件路径显示文件内容
        :param path: 文件路径
        """
        ext = os.path.splitext(path)[1].lower()
        try:
            if ext in ui_config.IMAGE_EXTENSIONS:
                # 确保图片视图有最小尺寸
                self.image_view.setMinimumSize(1, 1)

                # 加载图片
                pixmap = QPixmap(path)
                if pixmap.isNull():
                    self.image_view.setText("无法加载图片")
                else:
                    # 获取标签当前可用大小
                    available_size = self.image_view.size()

                    # 缩放图片以适应当前大小
                    scaled_pixmap = pixmap.scaled(
                        available_size,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )

                    # 设置图片
                    self.image_view.setPixmap(scaled_pixmap)

                # 切换到图片视图
                self.stack.setCurrentIndex(1)

            else:
                # 普通文本文件直接显示内容
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_view.setPlainText(content)
                self.stack.setCurrentIndex(0)
        except Exception as e:
            self.text_view.setPlainText(f"无法读取文件内容: {e}")
            self.stack.setCurrentIndex(0)


    def load_stylesheet(self):
        """加载样式表"""
        load_stylesheets(self, "explorer.css")


    def execute_commands(self):
        """
        执行命令文件
        """
        execute_command_file(self.current_file_path, self.text_view)

    def refresh_commands(self):
        self.display_file_content(self.current_file_path)
        info(True, "文件显示已刷新", True)