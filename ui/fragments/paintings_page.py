import io
import os
import sys

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QSplitter, QListWidget, QListWidgetItem
)

from configs.ui_config import ui_config
from tools.ui_tools.image_utils import get_scaled_pixmap
from tools.ui_tools.previewer import preview_command_file


class PaintingsPage(QWidget):
    """
    画作展示页面
    左侧显示 input 和 output 共有的文件夹名，右侧显示 input 中的 commands.txt 和 output 中的图片
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.load_common_names()
        # 存储当前选中的图片路径，用于窗口 resize 时重新缩放
        self.current_image_path = None

    # =============================================================
    # 界面初始化
    # ============================================================
    def init_ui(self):
        """
        初始化用户界面
        整体布局：
        - 主垂直布局 (QVBoxLayout)
          ├── 标题标签
          └── 水平布局 (QHBoxLayout)
              ├── 左侧名称列表 (QListWidget)
              └── 右侧分割器 (QSplitter)
                  ├── 命令文本区 (QTextEdit)
                  └── 图片展示区 (QLabel)
        """
        # 主垂直布局 - 作为顶层布局
        main_vertical_layout = QVBoxLayout()
        self.setLayout(main_vertical_layout)  # 设置为主布局

        # ==================================================
        # 标题栏
        # ==================================================
        label = QLabel("画作列表")
        label.setFixedHeight(28)  # 固定高度
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 12px;")
        main_vertical_layout.addWidget(label)

        # 主体水平布局 - 包含左侧列表和右侧内容区
        body_horizontal_layout = QHBoxLayout()
        # 注意：这里不再设置父对象，避免布局冲突
        body_horizontal_layout.setContentsMargins(4, 4, 4, 4)
        main_vertical_layout.addLayout(body_horizontal_layout)

        # 左侧列表 - 显示共有名称
        self.name_list = QListWidget()
        self.name_list.setMinimumWidth(200)
        body_horizontal_layout.addWidget(self.name_list)
        self.name_list.itemClicked.connect(self.on_name_clicked)

        # 右侧内容区 - 使用分割器
        splitter = QSplitter(Qt.Horizontal)
        body_horizontal_layout.addWidget(splitter, stretch=1)  # 占据剩余空间

        # 左半部分：commands.txt 预览
        self.commands_view = QTextEdit()
        self.commands_view.setReadOnly(True)
        splitter.addWidget(self.commands_view)

        # 右半部分：图片显示区域
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)
        self.image_view.setText("请选择左侧列表中的项目")
        self.image_view.setMinimumSize(1, 1)  # 允许缩小
        splitter.addWidget(self.image_view)

        # 设置分割器初始比例（命令区:图片区 = 1:2）
        splitter.setSizes([300, 600])

    # ==============================================================
    # 数据加载
    # ==============================================================
    def load_common_names(self):
        """
        加载 input 和 output 目录中公有的名称
        - 从 input 目录获取所有文件夹名称
        - 从 output 目录获取所有图片文件名称（不含扩展名）
        - 取交集后添加到左侧列表
        """
        input_path = os.path.join(QDir.currentPath(), "input")
        output_path = os.path.join(QDir.currentPath(), "output")
        image_exts = ui_config.IMAGE_EXTENSIONS

        # 获取 input 目录中的文件夹
        input_folders = []
        if os.path.exists(input_path):
            for item in os.listdir(input_path):
                item_path = os.path.join(input_path, item)
                if os.path.isdir(item_path):
                    input_folders.append(item)

        # 获取 output 目录中的图片文件（不含扩展名）
        output_image_names = []
        if os.path.exists(output_path):
            for item in os.listdir(output_path):
                item_path = os.path.join(output_path, item)
                if os.path.isfile(item_path):
                    name, ext = os.path.splitext(item)
                    if ext.lower() in image_exts:
                        output_image_names.append(name)

        # 取交集并排序添加到列表
        common_names = set(input_folders) & set(output_image_names)
        for name in sorted(common_names):
            self.name_list.addItem(QListWidgetItem(name))

    # ========================================================
    # 事件处理
    # =======================================================
    def on_name_clicked(self, item):
        """
        处理名称点击事件
        - 加载对应名称的 commands.txt 并显示
        - 查找并显示对应的输出图片
        """
        selected_name = item.text()
        input_folder = os.path.join(QDir.currentPath(), "input", selected_name)
        output_path = os.path.join(QDir.currentPath(), "output")
        image_exts = ui_config.IMAGE_EXTENSIONS

        # ================= 更新命令文本 =================
        commands_path = os.path.join(input_folder, "commands.txt")
        if os.path.exists(commands_path):
            try:
                # 重定向标准输出捕获预览内容
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

        # ================= 更新图片显示 =================
        target_image = None
        for ext in image_exts:
            candidate = os.path.join(output_path, f"{selected_name}{ext}")
            if os.path.exists(candidate):
                target_image = candidate
                break

        if target_image:
            self.current_image_path = target_image
            self.update_image_display()
        else:
            self.current_image_path = None
            self.image_view.setText(f"未找到 {selected_name} 对应的图片")

    # ============================================================
    # 图片显示处理
    # ===========================================================
    def update_image_display(self):
        """
        优化图片显示逻辑
        - 根据当前可用空间缩放图片
        - 保持纵横比
        - 确保图片不会过小（最小100x100像素）
        """
        if not self.current_image_path:
            return

        # 获取可用显示区域
        available_size = self.image_view.contentsRect().size()
        
        # 使用工具函数获取缩放后的图片
        scaled_pixmap, error_msg = get_scaled_pixmap(
            self.current_image_path,
            available_size
        )
        
        if scaled_pixmap:
            self.image_view.setPixmap(scaled_pixmap)
        else:
            self.image_view.setText(error_msg)

    # =======================================================================
    # 窗口事件处理
    # =======================================================================
    def resizeEvent(self, event: QResizeEvent):
        """
        窗口大小变化事件处理
        - 当窗口调整大小时重新缩放当前图片
        """
        super().resizeEvent(event)
        if self.current_image_path:
            self.update_image_display()