# 自动操作相关速度配置
MULTIPLIER_FACTOR = 1.0                     # 倍速因子，1.0表示正常速度

BASIC_DRAW_DURATION_1 = 0.5                   # 基础绘图持续时间（秒）
BASIC_DRAW_DURATION_2 = 0.3 
BASIC_DRAW_DURATION_3 = 0.2  
BASIC_CLICK_WAIT = 1                        # 基础点击等待时间（秒）
BASIC_MOUSE_MOVE_SPEED = 0.5                # 基础鼠标移动速度（像素/秒）
BASIC_EXTRA_MOVE_DELAY = 0.2                # 移动到起点后额外延迟，确保识别（秒）

ACTUAL_DRAW_DURATION = BASIC_DRAW_DURATION_1 / MULTIPLIER_FACTOR        # 实际绘图持续时间（秒）
ACTUAL_CLICK_WAIT = BASIC_CLICK_WAIT / MULTIPLIER_FACTOR                # 实际点击等待时间（秒）
ACTUAL_MOUSE_MOVE_SPEED = BASIC_MOUSE_MOVE_SPEED / MULTIPLIER_FACTOR    # 实际鼠标移动速度（像素/秒）
ACTUAL_EXTRA_MOVE_DELAY = BASIC_EXTRA_MOVE_DELAY / MULTIPLIER_FACTOR    # 实际额外移动延迟（秒）
ACTUAL_HALF_EXTRA_MOVE_DELAY = ACTUAL_EXTRA_MOVE_DELAY / 2              # 实际额外移动延迟的一半（秒）