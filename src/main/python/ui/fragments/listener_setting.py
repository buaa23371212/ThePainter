from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QLineEdit, QPushButton
)

from src.main.python.transcriber import ACTION_CHOICE


class ListenerSettingsWidget(QWidget):
    """监听器参数设置组件"""
    def __init__(self, file_manager, parent=None):
        super().__init__(parent)
        self.file_manager = file_manager
        self.init_ui()

    def init_ui(self):
        # 创建设置布局
        settings_layout = QVBoxLayout(self)
        settings_layout.setContentsMargins(10, 10, 10, 10)
        settings_layout.setSpacing(15)

        # 1. Action选择
        action_layout = QHBoxLayout()
        action_label = QLabel("操作类型:")
        self.action_combo = QComboBox()
        self.action_combo.addItems(ACTION_CHOICE)  # 根据实际需求添加选项
        self.action_combo.setCurrentText("record")  # 默认值
        action_layout.addWidget(action_label)
        action_layout.addWidget(self.action_combo)
        settings_layout.addLayout(action_layout)

        # 2. Input File设置
        input_layout = QHBoxLayout()
        self.input_file_edit = QLineEdit()
        self.input_file_edit.setPlaceholderText("输入文件路径（可选）")
        input_btn = QPushButton("浏览...")
        input_btn.clicked.connect(self._select_input_file)
        input_layout.addWidget(QLabel("输入文件:"))
        input_layout.addWidget(self.input_file_edit)
        input_layout.addWidget(input_btn)
        settings_layout.addLayout(input_layout)

        # 3. Output File设置
        output_layout = QHBoxLayout()
        self.output_file_edit = QLineEdit()
        self.output_file_edit.setPlaceholderText("输出文件路径（可选）")
        output_btn = QPushButton("浏览...")
        output_btn.clicked.connect(self._select_output_file)
        output_layout.addWidget(QLabel("输出文件:"))
        output_layout.addWidget(self.output_file_edit)
        output_layout.addWidget(output_btn)
        settings_layout.addLayout(output_layout)

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

    # 可以添加一些获取参数的方法，方便外部访问
    def get_action(self):
        """获取选中的操作类型"""
        return self.action_combo.currentText()

    def get_input_file(self):
        """获取输入文件路径"""
        return self.input_file_edit.text()

    def get_output_file(self):
        """获取输出文件路径"""
        return self.output_file_edit.text()