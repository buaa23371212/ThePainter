from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QLineEdit,
    QPushButton, QGroupBox, QScrollArea, QFrame, QSizePolicy, QTextEdit
)
from PyQt5.QtCore import Qt, QSize

from src.main.python.configs.ui_config import LABEL_WIDTH
from src.main.python.configs.project_config import json_dir, input_dir
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
        action_label = QLabel("操作类型:")
        action_label.setObjectName("listenerSettingActionLabel")
        action_label.setFixedWidth(LABEL_WIDTH)
        self.action_combo = QComboBox()
        self.action_combo.addItems(ACTION_CHOICE)
        
        debug(True, f"当前DEFAULT_ACTION_CHOICE值：{listener_config.DEFAULT_ACTION_CHOICE}")
        # TODO: [DEBUG] 当前DEFAULT_ACTION_CHOICE值："convert"
        self.action_combo.setCurrentText(listener_config.DEFAULT_ACTION_CHOICE)
        action_layout.addWidget(action_label)
        action_layout.addWidget(self.action_combo)
        settings_layout.addLayout(action_layout)

        # 2. Input File设置
        input_layout = QHBoxLayout()
        input_label = QLabel("输入文件:")
        input_label.setObjectName("listenerSettingInputLabel")
        input_label.setFixedWidth(LABEL_WIDTH)
        self.input_file_edit = QLineEdit()
        self.input_file_edit.setPlaceholderText("输入文件路径（可选）")
        input_btn = QPushButton("浏览...")
        input_btn.setObjectName("exploreBtn")
        input_btn.setFixedWidth(70)
        input_btn.clicked.connect(self._select_input_file)
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_file_edit)
        input_layout.addWidget(input_btn)
        settings_layout.addLayout(input_layout)

        # 3. Output File设置
        output_group = QGroupBox("输出文件设置")
        output_group_layout = QVBoxLayout(output_group)

        # 3.1 输出文件夹
        folder_layout = QHBoxLayout()
        folder_label = QLabel("保存文件夹:")
        folder_label.setObjectName("listenerSettingFolderLabel")
        folder_label.setFixedWidth(LABEL_WIDTH)
        self.output_folder_edit = QLineEdit()
        self.output_folder_edit.setPlaceholderText("输出文件夹路径（可选）")
        folder_btn = QPushButton("浏览...")
        folder_btn.setObjectName("exploreBtn")
        folder_btn.setFixedWidth(70)
        folder_btn.clicked.connect(self._select_output_folder)
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.output_folder_edit)
        folder_layout.addWidget(folder_btn)

        # 3.2 输出文件名
        filename_layout = QHBoxLayout()
        filename_label = QLabel("文件名称:")
        filename_label.setObjectName("listenerSettingFilenameLabel")
        filename_label.setFixedWidth(LABEL_WIDTH)
        self.output_filename_edit = QLineEdit()
        self.output_filename_edit.setPlaceholderText("输出文件名称（可选）")
        filename_layout.addWidget(filename_label)
        filename_layout.addWidget(self.output_filename_edit)

        # 将文件夹和文件名布局添加到输出文件组
        output_group_layout.addLayout(folder_layout)
        output_group_layout.addLayout(filename_layout)

        # 将输出文件组添加到设置布局
        settings_layout.addWidget(output_group)

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
        return """
        <p><strong>操作说明：</strong></p>
        <p><b>record</b>：记录并打印鼠标事件（默认）</p>
        <p><b>export</b>：记录并导出到文件</p>
        <p><b>convert</b>：记录并转换为绘图命令</p>
        <p><b>full</b>：记录、转换并打印绘图命令</p>
        <p><b>parse</b>：从文件解析并转换为绘图命令</p>
        <p><b>parse_and_save</b>：从文件解析、转换并保存绘图命令</p>
        
        <p><strong>使用提示：</strong></p>
        <p>1. 选择操作类型后，相关输入/输出字段会自动启用</p>
        <p>2. 对于需要输入文件的操作，请点击"浏览"按钮选择文件</p>
        <p>3. 对于需要输出文件的操作，请指定保存路径</p>
        <p>4. 操作执行结果将在输出面板显示</p>
        """

    def update_ui_state(self, action):
        """根据选择的action更新UI状态"""
        listener_config.DEFAULT_ACTION_CHOICE = f"\"{action}\""

        # 根据操作类型启用/禁用输入文件字段
        input_enabled = action in ['parse', 'parse_and_save']
        self.input_file_edit.setEnabled(input_enabled)

        # 根据操作类型启用/禁用输出文件相关字段
        output_enabled = action in ['export', 'parse_and_save']
        self.output_folder_edit.setEnabled(output_enabled)
        self.output_filename_edit.setEnabled(output_enabled)

        # 更新占位符文本
        if input_enabled:
            self.input_file_edit.setPlaceholderText("请选择输入文件")
        else:
            self.input_file_edit.setPlaceholderText("当前操作不需要输入文件")

        if output_enabled:
            if action == 'export':
                self.output_folder_edit.setPlaceholderText(json_dir)
                self.output_filename_edit.setPlaceholderText(listener_config.DEFAULT_JSON_NAME)
            if action == 'parse_and_save':
                self.output_folder_edit.setPlaceholderText(input_dir)
                self.output_filename_edit.setPlaceholderText(listener_config.DEFAULT_PCMD_NAME)
        else:
            self.output_folder_edit.setPlaceholderText("当前操作不需要输出文件夹")
            self.output_filename_edit.setPlaceholderText("当前操作不需要文件名")

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
        return self.output_file_edit.text().strip()