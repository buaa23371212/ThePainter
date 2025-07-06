from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel

class AIPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("AI作画")
        label.setFixedHeight(28)  # 固定高度
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 12px;")
        layout.addWidget(label)

        # 历史对话记录显示区
        self.history_box = QTextEdit()
        self.history_box.setReadOnly(True)
        self.history_box.setPlaceholderText("历史对话记录将在此显示...")
        self.history_box.setFixedHeight(120)
        layout.addWidget(self.history_box)

        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("请输入提示词...")
        input_layout.addWidget(self.input_box)

        self.send_btn = QPushButton("发送")
        input_layout.addWidget(self.send_btn)

        layout.addLayout(input_layout)