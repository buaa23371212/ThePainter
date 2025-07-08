import io
import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QTextEdit, QSplitter, QStackedWidget,
    QListWidget, QListWidgetItem
)
from PyQt5.QtCore import QDir, Qt, QSize
from PyQt5.QtGui import QPixmap, QResizeEvent

from utils.tools.previewer import preview_command_file

class PaintingsPage(QWidget):
    """
    面板，左侧显示 input 和 output 共有的文件夹名，右侧显示 input 中的 commands.txt 和 output 中的图片
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.load_common_names()
        # 存储当前选中的图片路径，用于窗口 resize 时重新缩放
        self.current_image_path = None

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(4, 4, 4, 4)

        # 左侧列表
        self.name_list = QListWidget()
        self.name_list.setMinimumWidth(200)
        main_layout.addWidget(self.name_list)
        self.name_list.itemClicked.connect(self.on_name_clicked)

        # 右侧内容区
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter, stretch=1)

        # 上半部分：commands.txt
        self.commands_view = QTextEdit()
        self.commands_view.setReadOnly(True)
        splitter.addWidget(self.commands_view)

        # 下半部分：图片显示（关键优化区域）
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)
        self.image_view.setText("请选择左侧列表中的项目")
        # 允许图片超出标签大小（配合缩放逻辑）
        self.image_view.setMinimumSize(1, 1)
        splitter.addWidget(self.image_view)

        # 记录分割器初始比例（让图片区域占更大空间）
        splitter.setSizes([300, 600])  # 上部分300px，下部分600px（可拖动调整）

    def load_common_names(self):
        # （保持不变，同之前的逻辑）
        input_path = os.path.join(QDir.currentPath(), "input")
        output_path = os.path.join(QDir.currentPath(), "output")

        input_folders = []
        if os.path.exists(input_path):
            for item in os.listdir(input_path):
                item_path = os.path.join(input_path, item)
                if os.path.isdir(item_path):
                    input_folders.append(item)

        output_image_names = []
        image_exts = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]
        if os.path.exists(output_path):
            for item in os.listdir(output_path):
                item_path = os.path.join(output_path, item)
                if os.path.isfile(item_path):
                    name, ext = os.path.splitext(item)
                    if ext.lower() in image_exts:
                        output_image_names.append(name)

        common_names = set(input_folders) & set(output_image_names)
        for name in sorted(common_names):
            self.name_list.addItem(QListWidgetItem(name))

    def on_name_clicked(self, item):
        selected_name = item.text()
        input_folder = os.path.join(QDir.currentPath(), "input", selected_name)
        output_path = os.path.join(QDir.currentPath(), "output")

        # 更新 commands.txt 显示（保持不变）
        commands_path = os.path.join(input_folder, "commands.txt")
        if os.path.exists(commands_path):
            try:
                buffer = io.StringIO()
                sys_stdout = sys.stdout
                sys.stdout = buffer
                preview_command_file(commands_path)
                sys.stdout = sys_stdout
                self.commands_view.setPlainText(buffer.getvalue())
            except Exception as e:
                self.commands_view.setPlainText(f"读取失败：{str(e)}")
        else:
            self.commands_view.setPlainText(f"未找到 commands.txt")

        # 更新图片显示（优化缩放逻辑）
        image_exts = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]
        target_image = None
        for ext in image_exts:
            candidate = os.path.join(output_path, f"{selected_name}{ext}")
            if os.path.exists(candidate):
                target_image = candidate
                break

        if target_image:
            self.current_image_path = target_image  # 记录当前图片路径
            self.update_image_display()  # 调用优化后的显示方法
        else:
            self.current_image_path = None
            self.image_view.setText(f"未找到 {selected_name} 对应的图片")

    def update_image_display(self):
        """优化图片显示逻辑，让图片尽可能大"""
        if not self.current_image_path:
            return

        pixmap = QPixmap(self.current_image_path)
        if pixmap.isNull():
            self.image_view.setText("图片加载失败")
            return

        # 获取图片显示区域的可用大小（减去边距）
        available_rect = self.image_view.contentsRect()
        available_size = available_rect.size()

        # 计算缩放后的尺寸：保持比例，不超过可用区域，最小边长不小于100
        scaled_size = pixmap.size().scaled(available_size, Qt.KeepAspectRatio)
        min_size = QSize(100, 100)  # 确保图片不会太小
        if scaled_size.width() < min_size.width():
            scaled_size.setWidth(min_size.width())
            scaled_size.setHeight(int(scaled_size.height() * (min_size.width() / scaled_size.width())))
        if scaled_size.height() < min_size.height():
            scaled_size.setHeight(min_size.height())
            scaled_size.setWidth(int(scaled_size.width() * (min_size.height() / scaled_size.height())))

        # 缩放并显示图片
        scaled_pixmap = pixmap.scaled(scaled_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_view.setPixmap(scaled_pixmap)

    def resizeEvent(self, event: QResizeEvent):
        """窗口大小变化时，重新缩放图片"""
        super().resizeEvent(event)
        if self.current_image_path:
            self.update_image_display()  # 窗口变化时重新调整图片大小