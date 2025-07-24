import io
import os
import sys

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QSplitter
)

from src.main.python.configs import ui_config
from src.main.python.configs.project_config import input_dir, output_dir
from src.main.python.configs.ui_config import TITLE_HEIGHT
from src.main.python.ui.fragments.navigate_bar import NavigationBar
from src.main.python.ui.utils.file_displayer import FileDisplayUtils
from src.main.python.ui.utils.previewer import preview_command_file


class PaintingsPage(QWidget):
    """
    画作展示页面
    左侧显示 input 和 output 共有的文件夹名，右侧显示 input 中的 commands.txt 和 output 中的图片
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # ====================================================================
        # STEP 1: 初始化成员变量
        # ====================================================================
        self.name_list = None          # 左侧名称列表控件
        self.commands_view = None      # 命令文本预览区
        self.image_view = None         # 图片展示区
        self.current_image_path = None # 当前选中的图片路径

        # ====================================================================
        # STEP 2: 初始化用户界面
        # ====================================================================
        self.init_ui()

    # ========================================================================
    # UI 初始化模块
    # ========================================================================
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
        # ====================================================================
        # STEP 1: 创建主布局
        # ====================================================================
        main_vertical_layout = QVBoxLayout()
        self.setLayout(main_vertical_layout)  # 设置为主布局
        main_vertical_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距

        # ====================================================================
        # STEP 2: 创建标题栏
        # ====================================================================
        label = QLabel("画作列表")
        label.setFixedHeight(TITLE_HEIGHT)          # 固定高度
        label.setObjectName("paintingTitleLabel")   # 添加对象名用于样式定制
        main_vertical_layout.addWidget(label)

        # ====================================================================
        # STEP 3: 创建主体水平布局
        # ====================================================================
        body_horizontal_layout = QHBoxLayout()
        body_horizontal_layout.setContentsMargins(4, 4, 4, 4)  # 设置内边距
        body_horizontal_layout.setSpacing(8)                   # 设置组件间距
        main_vertical_layout.addLayout(body_horizontal_layout)  # 添加到主布局

        # ====================================================================
        # STEP 4: 创建左侧名称列表
        # ====================================================================
        # 加载共有名称并创建导航栏
        self.name_list = NavigationBar(FileDisplayUtils.load_common_names(), 200)
        body_horizontal_layout.addWidget(self.name_list)  # 添加到水平布局

        # 连接点击事件
        self.name_list.itemClicked.connect(self.on_name_clicked)

        # ====================================================================
        # STEP 5: 创建右侧分割器
        # ====================================================================
        splitter = QSplitter(Qt.Horizontal)  # 水平分割器
        splitter.setChildrenCollapsible(False)  # 防止子组件被折叠
        body_horizontal_layout.addWidget(splitter, stretch=1)  # 占据剩余空间

        # ====================================================================
        # STEP 5.1: 创建命令文本预览区
        # ====================================================================
        self.commands_view = QTextEdit()
        self.commands_view.setReadOnly(True)  # 设置为只读
        self.commands_view.setPlaceholderText("选择左侧项目查看命令详情")  # 占位文本
        splitter.addWidget(self.commands_view)  # 添加到分割器左侧

        # ====================================================================
        # STEP 5.2: 创建图片展示区
        # ====================================================================
        self.image_view = QLabel()
        self.image_view.setAlignment(Qt.AlignCenter)  # 居中对齐
        self.image_view.setText("请选择左侧列表中的项目")  # 初始提示文本
        self.image_view.setMinimumSize(1, 1)  # 允许缩小
        splitter.addWidget(self.image_view)  # 添加到分割器右侧

        # ====================================================================
        # STEP 5.3: 设置分割器初始比例
        # ====================================================================
        splitter.setSizes([300, 600])  # 命令区:图片区 = 1:2

    # ========================================================================
    # 事件处理模块
    # ========================================================================
    def on_name_clicked(self, item):
        """
        处理名称点击事件
        - 加载对应名称的 commands.txt 并显示
        - 查找并显示对应的输出图片
        """
        # ====================================================================
        # STEP 1: 获取选中的名称
        # ====================================================================
        selected_name = item.text()

        # ====================================================================
        # STEP 2: 构建输入文件夹和输出路径
        # ====================================================================
        input_folder = os.path.join(input_dir, selected_name)
        output_path = output_dir
        image_exts = ui_config.IMAGE_EXTENSIONS

        # ====================================================================
        # STEP 3: 更新命令文本预览
        # ====================================================================
        commands_path = os.path.join(input_folder, "commands.txt")
        if os.path.exists(commands_path):
            try:
                # 重定向标准输出捕获预览内容
                buffer = io.StringIO()
                sys_stdout = sys.stdout
                sys.stdout = buffer

                # 预览命令文件
                preview_command_file(commands_path)

                # 恢复标准输出
                sys.stdout = sys_stdout

                # 设置预览文本
                self.commands_view.setPlainText(buffer.getvalue())
            except Exception as e:
                self.commands_view.setPlainText(f"读取失败：{str(e)}")
        else:
            self.commands_view.setPlainText(f"未找到 commands.txt")

        # ====================================================================
        # STEP 4: 更新图片显示
        # ====================================================================
        target_image = None

        # 查找匹配的图片文件
        for ext in image_exts:
            candidate = os.path.join(output_path, f"{selected_name}{ext}")
            if os.path.exists(candidate):
                target_image = candidate
                break

        if target_image:
            # 更新当前图片路径并显示图片
            self.current_image_path = target_image
            FileDisplayUtils.update_image_display(self.current_image_path, self.image_view)
        else:
            # 未找到图片时显示提示信息
            self.current_image_path = None
            self.image_view.setText(f"未找到 {selected_name} 对应的图片")

    # ========================================================================
    # 窗口事件处理模块
    # ========================================================================
    def resizeEvent(self, event: QResizeEvent):
        """
        窗口大小变化事件处理
        - 当窗口调整大小时重新缩放当前图片
        """
        super().resizeEvent(event)

        # ====================================================================
        # STEP 1: 检查是否有当前图片
        # ====================================================================
        if self.current_image_path:
            # ================================================================
            # STEP 2: 更新图片显示
            # ================================================================
            FileDisplayUtils.update_image_display(self.current_image_path, self.image_view)