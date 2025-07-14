from transcriber.src.utils.button_manager import ButtonManager
from transcriber.src.utils.button_recorder import ButtonRecorder

# 创建按钮管理器
manager = ButtonManager()

# 添加一些按钮
buttons = [
    ButtonRecorder("WinTaskbar", top=1020, bottom=1080, left=0, right=1920),
    ButtonRecorder("WindowMinimization", top=0, bottom=25, left=1740, right=1799)
]
manager.add_buttons(buttons)