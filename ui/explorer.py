import io
import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QTextEdit, QSplitter, QStackedWidget
)
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap

from ui.ui_tools.previewer import preview_command_file

class FileExplorer(QWidget):
    """
    资源管理器面板，只显示 input 和 output 文件夹内容，右侧显示文件内容
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
        self.stack = QStackedWidget()
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(self.text_view)  # index 0
        self.stack.addWidget(self.image_view) # index 1
        splitter.addWidget(self.stack)
        self.stack.setCurrentIndex(0)
        
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