import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QLineEdit,
    QPushButton, QGroupBox, QScrollArea, QFrame, QSizePolicy, QTextEdit
)
from PyQt5.QtCore import Qt, QSize

from src.main.python.configs.ui_config import LABEL_WIDTH
from src.main.python.configs.project_config import json_dir, input_dir
from src.main.python.ui.fragments import HELP_CONTENT
from src.main.python.utils.listener_manager import listener_config
from src.main.python.terminal_logger.logger import debug
from src.main.python.transcriber import ACTION_CHOICE

class ListenerSettingsWidget(QWidget):
    """监听器参数设置组件 - 重新设计版本"""
    def __init__(self, file_manager, parent=None):
        super().__init__(parent)
        self.file_manager = file_manager
        self.init_ui()

        # 根据操作类型更新UI状态
        self.action_combo.currentTextChanged.connect(self.update_ui_state)

    def init_ui(self):
        # 主布局 - 水平布局（左侧设置框 + 右侧帮助信息）
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(20)

        # 左侧：设置框
        settings_container = QFrame()
        settings_container.setObjectName("settingsContainer")
        settings_container.setFrameShape(QFrame.StyledPanel)

        # 设置框布局
        settings_layout = QVBoxLayout(settings_container)
        settings_layout.setContentsMargins(10, 10, 10, 10)
        settings_layout.setSpacing(15)

        # 标题
        title_label = QLabel("监听器参数设置")
        title_label.setObjectName("listenerSettingTitleLabel")
        settings_layout.addWidget(title_label)

        # 1. Action选择
        action_layout = QHBoxLayout()
        action_label = self._create_label("操作类型:", "listenerSettingActionLabel")
        self.action_combo = QComboBox()
        self.action_combo.addItems(ACTION_CHOICE)
        
        debug(False, f"当前DEFAULT_ACTION_CHOICE值：{repr(listener_config.DEFAULT_ACTION_CHOICE)}")
        self.action_combo.setCurrentText(listener_config.DEFAULT_ACTION_CHOICE)
        action_layout.addWidget(action_label)
        action_layout.addWidget(self.action_combo)
        settings_layout.addLayout(action_layout)

        # 2. Input File设置
        self.input_widget = QWidget()
        input_layout = QHBoxLayout(self.input_widget)
        input_label = self._create_label("输入文件:", "listenerSettingInputLabel")
        self.input_file_edit = self._create_edit_line("输入文件路径（可选）")
        input_btn = self._create_btn("浏览...", "exploreBtn", 70, self._select_input_file)
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_file_edit)
        input_layout.addWidget(input_btn)
        settings_layout.addWidget(self.input_widget)

        # 3. Output File设置
        self.output_group = QGroupBox("输出文件设置")
        output_group_layout = QVBoxLayout(self.output_group)

        # 3.1 输出文件夹
        folder_layout = QHBoxLayout()
        folder_label = self._create_label("保存文件夹:", "listenerSettingFolderLabel")
        self.output_folder_edit = self._create_edit_line("输出文件夹路径（可选）")
        folder_btn = self._create_btn("浏览...", "exploreBtn", 70, self._select_output_folder)
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.output_folder_edit)
        folder_layout.addWidget(folder_btn)

        # 3.2 输出画作名
        painting_name_layout = QHBoxLayout()
        self.painting_name_label = self._create_label("画作名:", "listenerSettingPaintingNameLabel")
        self.painting_name_edit = self._create_edit_line("输出画作名称（可选）")
        painting_name_layout.addWidget(self.painting_name_label)
        painting_name_layout.addWidget(self.painting_name_edit)

        # 3.3 输出文件名
        filename_layout = QHBoxLayout()
        filename_label = self._create_label("文件名称:", "listenerSettingFilenameLabel")
        self.output_filename_edit = self._create_edit_line("输出文件名称（可选）")
        filename_layout.addWidget(filename_label)
        filename_layout.addWidget(self.output_filename_edit)

        # 将文件夹和文件名布局添加到输出文件组
        output_group_layout.addLayout(folder_layout)
        output_group_layout.addLayout(painting_name_layout)
        output_group_layout.addLayout(filename_layout)

        # 将输出文件组添加到设置布局
        settings_layout.addWidget(self.output_group)

        # 添加弹性空间
        settings_layout.addStretch(1)

        # 右侧：帮助信息框
        help_container = QFrame()
        help_container.setObjectName("helpContainer")
        help_container.setFrameShape(QFrame.StyledPanel)

        # 帮助信息布局
        help_layout = QVBoxLayout(help_container)
        help_layout.setContentsMargins(10, 10, 10, 10)

        # 帮助标题
        help_title = QLabel("操作说明")
        help_title.setObjectName("listenerSettingHelpTitle")
        help_layout.addWidget(help_title)

        # 帮助内容
        help_content = QTextEdit(self.get_help_text())
        help_content.setReadOnly(True)
        help_content.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        help_layout.addWidget(help_content)

        # 将设置框和帮助框添加到主布局
        main_layout.addWidget(settings_container)
        main_layout.addWidget(help_container)

        # 初始UI状态
        self.update_ui_state(self.action_combo.currentText())

    def get_help_text(self):
        """返回格式化的帮助文本"""
        return HELP_CONTENT
    
    def _create_label(self, text, object_name):
        """创建标签的工具方法"""
        label = QLabel(text)
        label.setObjectName(object_name)
        label.setFixedWidth(LABEL_WIDTH)
        return label
    
    def _create_btn(self, text, object_name, fixed_width, clicked_callback):
        """创建按钮的工具方法"""
        btn = QPushButton(text)
        btn.setObjectName(object_name)
        btn.setFixedWidth(fixed_width)
        btn.clicked.connect(clicked_callback)
        return btn
    
    def _create_edit_line(self, text):
        edit_line = QLineEdit()
        edit_line.setPlaceholderText(text)
        return edit_line

    def update_ui_state(self, action):
        """根据选择的action更新UI状态"""
        # 保存当前操作类型
        listener_config.DEFAULT_ACTION_CHOICE = action
        
        # 清空所有编辑框
        self.input_file_edit.clear()
        self.output_folder_edit.clear()
        self.painting_name_edit.clear()
        self.output_filename_edit.clear()
        
        # 根据操作类型设置输入输出状态
        input_enabled = action in ['parse', 'parse_and_save']
        output_enabled = action in ['export', 'parse_and_save']
        
        # 设置输入部分可见性和状态
        self.input_widget.setVisible(input_enabled)
        if input_enabled:
            self.input_file_edit.setEnabled(True)
            self.input_file_edit.setPlaceholderText("请选择输入文件")
        else:
            self.input_file_edit.setEnabled(False)
            self.input_file_edit.setPlaceholderText("当前操作不需要输入文件")
        
        # 设置输出部分可见性和状态
        self.output_group.setVisible(output_enabled)
        if output_enabled:
            # 设置输出部分默认值
            if action == 'export':
                self.output_folder_edit.setText(json_dir)
                self.output_filename_edit.setText(listener_config.DEFAULT_JSON_NAME)
                # 隐藏画作名相关控件
                self.painting_name_label.setVisible(False)
                self.painting_name_edit.setVisible(False)
            elif action == 'parse_and_save':
                self.output_folder_edit.setText(input_dir)
                self.painting_name_edit.setText("Sample-1")
                self.output_filename_edit.setText(listener_config.DEFAULT_PCMD_NAME)
                # 显示画作名相关控件
                self.painting_name_label.setVisible(True)
                self.painting_name_edit.setVisible(True)
            
            # 启用输出部分控件
            self.output_folder_edit.setEnabled(True)
            self.painting_name_edit.setEnabled(True)
            self.output_filename_edit.setEnabled(True)
        else:
            # 禁用输出部分控件
            self.output_folder_edit.setEnabled(False)
            self.painting_name_edit.setEnabled(False)
            self.output_filename_edit.setEnabled(False)
            self.output_folder_edit.setPlaceholderText("当前操作不需要输出文件夹")
            self.output_filename_edit.setPlaceholderText("当前操作不需要文件名")
        
        # 保存输出状态供其他方法使用
        self.output_enabled = output_enabled

    def _select_input_file(self):
        """选择输入文件"""
        file_path = self.file_manager.open_file()
        if file_path:
            self.input_file_edit.setText(file_path)

    def _select_output_file(self):
        """选择输出文件"""
        file_path = self.file_manager.save_file()
        if file_path:
            self.output_file_edit.setText(file_path)

    def _select_output_folder(self):
        """选择输出文件夹"""
        folder_path = self.file_manager.choose_directory()  # 需要在FileManager中实现此方法
        if folder_path:
            self.output_folder_edit.setText(folder_path)

    def get_action(self):
        """获取选中的操作类型"""
        return self.action_combo.currentText()

    def get_input_file(self):
        """获取输入文件路径"""
        return self.input_file_edit.text().strip()

    def get_output_file(self):
        """获取输出文件路径"""
        # 获取各字段值，为空时使用默认占位符或空字符串
        folder = self.output_folder_edit.text().strip()
        painting_name = self.painting_name_edit.text().strip()
        filename = self.output_filename_edit.text().strip()

        debug(True, f"{folder}, {painting_name}, {filename}")

        # 过滤空值（避免多余的路径层级）
        path_parts = [part for part in [folder, painting_name, filename] if part]

        debug(True, path_parts)

        if not self.output_enabled:
            return ""
        
        if self.output_enabled and not path_parts:
            raise ValueError("输出文件路径无效：文件夹、画作名和文件名不能同时为空")
        
        return os.path.join(*path_parts)