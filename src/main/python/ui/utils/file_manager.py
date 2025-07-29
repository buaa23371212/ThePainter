# file_tree_utils.py
import os
import tkinter as tk
from tkinter import filedialog
from typing import Optional, List
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem

from src.main.python.configs.project_config import json_dir

class FileTreeUtils:
    """文件树操作工具类"""

    @staticmethod
    def build_file_tree(tree_widget, root_paths, folder_icon="folder_icon.png", file_icon="file_icon.png"):
        """
        构建文件树结构
        :param tree_widget: 目标树形控件
        :param root_paths: 根路径列表
        :param folder_icon: 文件夹图标路径
        :param file_icon: 文件图标路径
        """
        for path in root_paths:
            if os.path.exists(path):
                folder_name = os.path.basename(path)
                folder_item = QTreeWidgetItem([folder_name])
                tree_widget.addTopLevelItem(folder_item)
                FileTreeUtils._add_children(folder_item, path, folder_icon, file_icon)

    @staticmethod
    def _add_children(parent_item, folder_path, folder_icon, file_icon):
        """
        递归添加子文件和子文件夹到树形控件
        :param parent_item: 父节点
        :param folder_path: 当前文件夹路径
        :param folder_icon: 文件夹图标路径
        :param file_icon: 文件图标路径
        """
        for name in os.listdir(folder_path):
            path = os.path.join(folder_path, name)
            child_item = QTreeWidgetItem([name])

            # 设置图标
            if os.path.isdir(path):
                child_item.setIcon(0, QIcon(folder_icon))
            else:
                child_item.setIcon(0, QIcon(file_icon))

            # 存储完整路径到用户数据
            child_item.setData(0, Qt.UserRole, path)
            parent_item.addChild(child_item)

            # 如果是文件夹，递归添加其内容
            if os.path.isdir(path):
                FileTreeUtils._add_children(child_item, path, folder_icon, file_icon)

class FileManager:
    """文件管理类，封装文件选择相关功能"""

    def __init__(self, root: tk.Tk):
        """初始化文件管理器

        Args:
            root: 父窗口（Tkinter 主窗口实例）
        """
        self.root = root
        # 可选：记录最近打开的文件路径
        self.recent_files: List[str] = []

    def open_file(self, file_types: Optional[List[tuple]] = None) -> Optional[str]:
        """打开文件选择对话框，返回选中的文件路径

        Args:
            file_types: 文件类型过滤，格式如 [("文本文件", "*.txt"), ("所有文件", "*.*")]

        Returns:
            选中的文件路径（字符串），取消选择则返回 None
        """
        # 默认文件类型（所有文件）
        default_file_types = [("所有文件", "*.*")]
        selected_types = file_types if file_types else default_file_types

        # 打开文件对话框
        file_path = filedialog.askopenfilename(
            parent=self.root,
            title="选择文件",
            filetypes=selected_types,
            initialdir=json_dir
        )

        # 如果选择了文件，记录到最近文件列表
        if file_path:
            self._add_recent_file(file_path)

        return file_path

    def save_file(self, default_filename: str = "", file_types: Optional[List[tuple]] = None) -> Optional[str]:
        """打开保存文件对话框，返回保存路径

        Args:
            default_filename: 默认文件名
            file_types: 文件类型过滤

        Returns:
            保存路径（字符串），取消则返回 None
        """
        default_file_types = [("所有文件", "*.*")]
        selected_types = file_types if file_types else default_file_types

        file_path = filedialog.asksaveasfilename(
            parent=self.root,
            title="保存文件",
            defaultextension="",  # 不自动添加扩展名（如需自动添加可指定，如 ".txt"）
            initialfile=default_filename,
            filetypes=selected_types
        )

        return file_path

    def _add_recent_file(self, file_path: str) -> None:
        """将文件路径添加到最近文件列表（去重并限制长度）"""
        # 去重：如果已存在则移到列表首位
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        self.recent_files.insert(0, file_path)
        # 限制最近文件列表长度为10
        if len(self.recent_files) > 10:
            self.recent_files.pop()

    def get_recent_files(self) -> List[str]:
        """获取最近打开的文件列表"""
        return self.recent_files.copy()
    
    def choose_directory(self) -> Optional[str]:
        """打开文件夹选择对话框，返回选中的文件夹路径"""
        directory = filedialog.askdirectory(
            parent=self.root,
            title="选择文件夹"
        )
        return directory if directory else None