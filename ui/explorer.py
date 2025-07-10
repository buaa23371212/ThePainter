import io
import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QTextEdit, 
    QSplitter, QStackedWidget, QPushButton, QHBoxLayout, QFrame
)
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap

from ui.ui_tools.previewer import preview_command_file

from painter_tools.terminal_logger.logger import info, warn, error, debug

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
        
        # TODO: 加载样式表
        # self.load_stylesheet()

        # ==================================================
        # 标题栏
        # ==================================================
        title_label = QLabel("资源管理器")
        title_label.setFixedHeight(28)  # 固定高度
        title_label.setStyleSheet("""
            font-size: 16px; 
            font-weight: bold; 
            margin: 4px;
            border-bottom: 1px solid #ddd;
        """)
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
        self.tree.setColumnWidth(200, 250)        # 设置列宽
        splitter.addWidget(self.tree)           # 添加到分割器左侧
        
        # 设置树形控件的样式
        self.tree.setStyleSheet("""
            QTreeWidget {
                border: 1px solid #ccc;
                border-radius: 4px;
            }
        """)

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
        self.toolbar.setStyleSheet("""
            background-color: #f0f0f0;
            border-bottom: 1px solid #ddd;
            padding: 4px;
        """)
        self.toolbar.setVisible(False)  # 默认隐藏
        
        toolbar_layout = QHBoxLayout(self.toolbar)
        toolbar_layout.setAlignment(Qt.AlignRight)
        
        # 执行按钮
        self.execute_btn = QPushButton("执行命令")
        self.execute_btn.setFixedSize(100, 30)
        self.execute_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.execute_btn.clicked.connect(self.execute_commands)
        toolbar_layout.addWidget(self.execute_btn)
        
        right_layout.addWidget(self.toolbar)
        
        # 预览区域
        self.stack = QStackedWidget()
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(self.text_view)  # index 0
        self.stack.addWidget(self.image_view) # index 1
        right_layout.addWidget(self.stack)
        self.stack.setCurrentIndex(0)
        
        splitter.addWidget(right_container)
        
        # 设置分割比例：右侧区域可伸缩（占比更大）
        splitter.setStretchFactor(1, 1)         # 索引1（右侧）的伸缩因子为1

        # =====================================================
        # 初始化文件树结构
        # =====================================================
        # 只显示 input 和 output 文件夹
        for folder in ["input", "output"]:
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
        
        # 如果是命令文件，显示工具栏
        if path and os.path.isfile(path) and path.endswith('.pcmd'):
            self.toolbar.setVisible(True)
        else:
            self.toolbar.setVisible(False)
        
        # 如果点击的是文件
        if path and os.path.isfile(path):
            ext = os.path.splitext(path)[1].lower()
            try:
                if ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]:
                    pixmap = QPixmap(path)
                    if pixmap.isNull():
                        self.image_view.setText("无法加载图片")
                    else:
                        self.image_view.setPixmap(pixmap.scaled(
                            self.image_view.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
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
        else:
            # 点击的是文件夹时清空预览区
            self.text_view.clear()
            self.stack.setCurrentIndex(0)


    def load_stylesheet(self):
        """加载样式表"""
        try:
            # 获取当前文件所在目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            css_dir = os.path.join(current_dir, "css")
            css_path = os.path.join(css_dir, "styles.css")
            
            if os.path.exists(css_path):
                with open(css_path, "r", encoding="utf-8") as f:
                    stylesheet = f.read()
                    self.setStyleSheet(stylesheet)
                info(False, "样式表加载成功", True)

                debug(True, f"全局样式表内容:\n{self.styleSheet()}", True)
            else:
                warn(True, f"CSS文件不存在: {css_path}", True)
        except Exception as e:
            error(True, f"加载样式表失败: {str(e)}", True)


    def execute_commands(self):
        """
        执行命令文件
        """
        if self.current_file_path and os.path.isfile(self.current_file_path):
            # TODO: 这里需要实现实际的命令执行逻辑
            info(True, f"执行命令文件: {self.current_file_path}", True)
            
            # 在实际应用中，您可能需要调用类似这样的函数：
            # from command_handler.command_executor import process_batch_commands
            # process_batch_commands(self.current_file_path)
            
            # 显示执行状态
            self.text_view.append("\n\n=== 命令执行开始 ===")
            self.text_view.append(f"执行文件: {os.path.basename(self.current_file_path)}")
            self.text_view.append("状态: 执行成功 (模拟)")
            self.text_view.append("=== 命令执行结束 ===")
        else:
            error(True, "没有可执行的命令文件", True)