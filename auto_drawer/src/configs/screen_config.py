"""
屏幕和画布配置信息
"""
from public_utils.terminal_logger.logger import info

# ======================
# 自定义部分
# ======================
# 屏幕尺寸
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# 画布边界
CANVAS_TOP = 270       # 画布顶部位置
CANVAS_BOTTOM = 920    # 画布底部位置
CANVAS_LEFT = 380      # 画布左侧位置

# 画布内边距
CANVAS_PADDING = 10    # 画布边界与画布内容的间距

# 点击激活窗口
WINDOW_ACTIVATE_POSITION = (1000, 50)

# 画布空白位置
CANVAS_BLANK_POSITION = (100, 500)

# ======================
# 计算部分
# ======================
# 屏幕中心点
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# 计算画布尺寸
CANVAS_WIDTH = SCREEN_WIDTH - 2 * CANVAS_LEFT  # 左右对称
CANVAS_HEIGHT = CANVAS_BOTTOM - CANVAS_TOP

# 画布中心点
CANVAS_CENTER = (SCREEN_CENTER[0], (CANVAS_TOP + CANVAS_BOTTOM) // 2)

# 画布边界
CANVAS_RIGHT = SCREEN_WIDTH - CANVAS_LEFT  # 左右对称

# 计算可用绘图区域（考虑内边距）
CANVAS_DRAWABLE_LEFT = CANVAS_LEFT + CANVAS_PADDING
CANVAS_DRAWABLE_TOP = CANVAS_TOP + CANVAS_PADDING
CANVAS_DRAWABLE_RIGHT = CANVAS_RIGHT - CANVAS_PADDING
CANVAS_DRAWABLE_BOTTOM = CANVAS_BOTTOM - CANVAS_PADDING
CANVAS_DRAWABLE_WIDTH = CANVAS_DRAWABLE_RIGHT - CANVAS_DRAWABLE_LEFT
CANVAS_DRAWABLE_HEIGHT = CANVAS_DRAWABLE_BOTTOM - CANVAS_DRAWABLE_TOP

# ======================
# 图层模式下的计算
# ======================

# 计算图层模式下画布中心点
CANVAS_LAYER_MODE_CENTER = (CANVAS_CENTER[0] - 85, CANVAS_CENTER[1])
info(False,
     f"画布中心点：{CANVAS_LAYER_MODE_CENTER}",
     True)

# 计算图层模式下可用绘画区域(实际绘图区域整体向左平移了50像素)
CANVAS_LAYER_MODE_DRAWABLE_LEFT = CANVAS_DRAWABLE_LEFT - 80
CANVAS_LAYER_MODE_DRAWABLE_RIGHT = CANVAS_DRAWABLE_RIGHT - 90
CANVAS_LAYER_MODE_DRAWABLE_TOP = CANVAS_DRAWABLE_TOP
CANVAS_LAYER_MODE_DRAWABLE_BOTTOM = CANVAS_DRAWABLE_BOTTOM
CANVAS_LAYER_MODE_DRAWABLE_WIDTH = CANVAS_DRAWABLE_WIDTH
CANVAS_LAYER_MODE_DRAWABLE_HEIGHT = CANVAS_DRAWABLE_HEIGHT

info(False,
     "\n可用绘画区域：\n"
     + f"左侧：{CANVAS_LAYER_MODE_DRAWABLE_LEFT}\n"
     + f"右侧：{CANVAS_LAYER_MODE_DRAWABLE_RIGHT}\n"
     + f"顶部：{CANVAS_LAYER_MODE_DRAWABLE_TOP}\n"
     + f"底部：{CANVAS_LAYER_MODE_DRAWABLE_BOTTOM}\n",
     True)

# ==============================================
# 图层模式下可绘画区域：
# (310, 280)
# ┌───────────────────────────────────────────────────────┐
# │ 顶部: 280px                                           │
# │ 左侧: 310px                     宽度: 1130px          │
# │ 底部: 910px                                           │
# │ 右侧: 1440px                                          │
# └───────────────────────────────────────────────────────┘
#                                                       (1440, 910)
# 注意：画地平线时为了防止颜色填充错误应该从left=300画到right=1450，即将减去的内边距加回来
# ==============================================