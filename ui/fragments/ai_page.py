from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import QTimer

class AIPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # ==================================================
        # 标题栏
        # ==================================================
        label = QLabel("AI作画")
        label.setFixedHeight(28)  # 固定高度
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 12px;")
        layout.addWidget(label)

        # ==================================================
        # 历史对话记录显示区
        # ==================================================
        self.history_box = QTextEdit()
        self.history_box.setReadOnly(True)
        self.history_box.setPlaceholderText("历史对话记录将在此显示...")
        layout.addWidget(self.history_box)

        # ==================================================
        # 输入框和发送按钮
        # ==================================================
        input_layout = QHBoxLayout()
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("请输入提示词...")
        self.input_box.setFixedHeight(120)
        input_layout.addWidget(self.input_box)

        self.send_btn = QPushButton("发送")
        self.send_btn.clicked.connect(self.on_send_clicked)  # 连接点击信号
        self.send_btn.setFixedHeight(120)
        input_layout.addWidget(self.send_btn)

        layout.addLayout(input_layout)

    # ========================================================
    # 事件处理
    # =======================================================
    def on_send_clicked(self):
        """处理发送按钮点击事件"""
        # 1. 获取用户输入
        user_input = self.input_box.toPlainText().strip()
        
        if not user_input:
            return  # 忽略空输入
        
        # 2. 清空输入框
        self.input_box.clear()
        
        # 3. 在历史记录中显示用户消息
        self.append_message("用户", user_input)
        
        # 4. 模拟AI处理（1秒后回复）
        QTimer.singleShot(1000, lambda: self.show_ai_response())

    def append_message(self, sender, message):
        """在历史记录框中添加消息"""
        formatted_message = f"<b>{sender}:</b> {message}<br>"
        self.history_box.append(formatted_message)
    
    # ========================================================
    # AI回复处理
    # =======================================================
    def show_ai_response(self):
        """显示AI回复"""
        ai_response = "已生成commands.txt和配套的shapes.json，随时可以执行"
        self.append_message("AI", ai_response)
