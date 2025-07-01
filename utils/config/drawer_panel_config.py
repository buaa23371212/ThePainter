# 画图工具操作面板的快捷键配置
from utils.config import screen_config

# TODO
# 形状按钮在工具栏上的位置（即直线按钮位置）
SHAPES_BUTTON_POSITION = (screen_config.SCREEN_WIDTH // 4 + 65, 95)

# 图层相关按钮位置
LAYERS_BUTTON_POSITION = (1440, 130)         # 图层按钮位置
ADD_LAYER_BUTTON_POSITION = (1830, 260)      # 添加图层按钮位置

# 图层视图的高度
# 例如点击第一个图层按钮时，鼠标需移动到添加图层按钮的下方100像素位置
# 且第一个图层为顶部图层
LAYER_VIEW_HEIGHT = 100
FIRST_LAYER_VIEW_POSITION = (ADD_LAYER_BUTTON_POSITION[0], ADD_LAYER_BUTTON_POSITION[1] + LAYER_VIEW_HEIGHT)

# 右键后在原地弹出图层操作菜单
# 例如：点击第一个选项时，鼠标移动到右键位置的向左200像素，向下25像素位置
# 点击第二个选项时，向下移动40像素
RIGHT_CLICK_OFFSET = (200, 25)              # 右键菜单偏移位置
OPTION_BOX_PADDING = 5                      # 选项内边距

# 选项卡高度
TAB_HEIGHT = 40

# 每种选项对应按下方向键的次数
TAB_KEY_MAP = {
    "hide": 0,              # 隐藏/显示图层
    "copy": 1,              # 复制图层
    "merge_down": 2,        # 向下合并
    "move_up": 3,           # 上移
    "move_down": 4,         # 下移
    "delete": 5,            # 删除图层
}

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
    若形状不在预设列表中，则返回-1

    :param shape: 形状名称
    :return: 按右方向键的次数
    """
    return SHAPE_PANEL_KEY_MAP.get(shape, -1)

def get_tab_key_presses(operation: str) -> int:
    """
    获取执行指定图层操作时需要按下方向键的次数
    若操作不在预设列表中，则返回-1

    :param operation: 图层操作名称
    :return: 按下方向键的次数
    """
    return TAB_KEY_MAP.get(operation, -1)