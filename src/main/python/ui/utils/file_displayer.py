import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize, QDir
from PyQt5.QtWidgets import QLabel

from src.main.python.configs import ui_config
from src.main.python.configs.project_config import input_dir, output_dir


def get_scaled_pixmap(image_path, container_size, min_size=QSize(100, 100)):
    """
    获取缩放后的图片
    
    参数:
        image_path: 图片文件路径
        container_size: 容器尺寸 (QSize)
        min_size: 最小显示尺寸 (默认 100x100)
    
    返回:
        QPixmap: 缩放后的图片对象
        str: 错误信息（成功时返回空字符串）
    """
    if not image_path:
        return None, "无图片路径"
    
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        return None, "图片加载失败"
    
    # 计算缩放尺寸（保持比例）
    scaled_size = pixmap.size().scaled(
        container_size, 
        Qt.KeepAspectRatio
    )
    
    # 确保不小于最小尺寸
    if scaled_size.width() < min_size.width():
        scale_factor = min_size.width() / scaled_size.width()
        scaled_size = QSize(
            min_size.width(),
            int(scaled_size.height() * scale_factor)
        )
    if scaled_size.height() < min_size.height():
        scale_factor = min_size.height() / scaled_size.height()
        scaled_size = QSize(
            int(scaled_size.width() * scale_factor),
            min_size.height()
        )
    
    # 应用缩放
    return pixmap.scaled(
        scaled_size, 
        Qt.KeepAspectRatio, 
        Qt.SmoothTransformation
    ), ""


class FileDisplayUtils:
    """文件显示工具类，用于处理不同类型文件的内容展示"""
    _instance = None  # 存储唯一实例

    def __new__(cls, *args, **kwargs):
        # 确保只创建一个实例
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # 初始化实例属性（仅在首次创建时执行）
        self.input_folders = []
        self.output_image_names = []

    def display_file_content(self, path, text_view, image_view, stack):
        """
        根据文件路径显示文件内容到指定的视图组件

        :param path: 文件路径
        :param text_view: 文本显示组件
        :param image_view: 图片显示组件
        :param stack: 用于切换视图的QStackedWidget
        """
        ext = os.path.splitext(path)[1].lower()
        try:
            if ext in ui_config.IMAGE_EXTENSIONS:
                # 确保图片视图有最小尺寸
                image_view.setMinimumSize(1, 1)

                # 加载图片
                pixmap = QPixmap(path)
                if pixmap.isNull():
                    image_view.setText("无法加载图片")
                else:
                    # 获取标签当前可用大小
                    available_size = image_view.size()

                    # 缩放图片以适应当前大小
                    scaled_pixmap = pixmap.scaled(
                        available_size,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )

                    # 设置图片
                    image_view.setPixmap(scaled_pixmap)

                # 切换到图片视图
                stack.setCurrentIndex(1)

            else:
                # 普通文本文件直接显示内容
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                text_view.setPlainText(content)
                stack.setCurrentIndex(0)
        except Exception as e:
            text_view.setPlainText(f"无法读取文件内容: {e}")
            stack.setCurrentIndex(0)

    def load_common_names(self):
        """
        加载 input 和 output 目录中公有的名称
        - 从 input 目录获取所有文件夹名称
        - 从 output 目录获取所有图片文件名称（不含扩展名）
        - 取交集后添加到左侧列表
        """
        input_path = input_dir
        output_path = output_dir
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
        sorted_common_names = sorted(common_names)  # 默认按字母升序排序

        return sorted_common_names

    def update_image_display(self, image_path, image_label: QLabel):
        """
        优化图片显示逻辑
        - 根据当前可用空间缩放图片
        - 保持纵横比
        - 确保图片不会过小（最小100x100像素）
        """
        if not image_path:
            return

        # 获取可用显示区域
        available_size = image_label.contentsRect().size()

        # 使用工具函数获取缩放后的图片
        scaled_pixmap, error_msg = get_scaled_pixmap(
            image_path,
            available_size
        )

        if scaled_pixmap:
            image_label.setPixmap(scaled_pixmap)
        else:
            image_label.setText(error_msg)

file_display_utils = FileDisplayUtils()