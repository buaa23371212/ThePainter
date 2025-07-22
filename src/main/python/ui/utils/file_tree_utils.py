# file_tree_utils.py
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem

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