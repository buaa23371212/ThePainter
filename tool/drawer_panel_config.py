# 画图工具操作面板的快捷键配置
from tool import screen_config

# 形状按钮在屏幕上的相对位置（相对于屏幕宽高）
SHAPES_BUTTON_POSITION = (screen_config.SCREEN_WIDTH // 4 + 65, 95)

# 每种形状对应按右方向键的次数
SHAPE_PANEL_KEY_MAP = {
    "line": 0,              # 直线
    "ellipse": 2,           # 椭圆
    "circle": 2,            # 圆
    "rectangle": 3,         # 矩形
    "square": 3,            # 正方形
    "rounded_rectangle": 4, # 圆角矩形
    "polygon": 5,           # 多边形
}

def get_shape_panel_presses(shape: str) -> int:
    """
    获取选择指定形状工具时需要按右方向键的次数
    :param shape: 形状名称
    :return: 按右方向键的次数
    """
    return SHAPE_PANEL_KEY_MAP.get(shape, 0)