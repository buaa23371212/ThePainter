# 画图工具操作面板的快捷键配置
from auto_drawer.src.configs import screen_config

# ============================================
# 工具类型配置模块
# ============================================

# 支持的工具类型
TOOL_TYPE_LIST = [
    "shape",   # 图形绘制工具
    "fill",    # 填充工具
    "brush",   # 画笔工具
    "layer"    # 图层操作工具
]

SHAPES_BUTTON_POSITION = (screen_config.SCREEN_WIDTH // 4 + 65, 95)         # 形状按钮在工具栏上的位置（以直线按钮为基准）

LAYERS_BUTTON_POSITION = (1440, 130)                                        # 进入图层模式按钮位置（屏幕坐标）

FILL_TOOL_POSITION = (360, 100)                                             # 填充工具（颜料桶）位置（屏幕坐标）

TEXT_TOOL_POSITION = (410, 100)                                             # 文本工具位置（屏幕坐标）

# ============================================
# 形状工具配置模块
# ============================================

# 形状选择快捷键映射表（按键次数 = 右方向键按下次数）
SHAPE_PANEL_KEY_MAP = {
    "line": 0,              # 直线（初始位置）
    "curve": 1,             # 曲线
    "ellipse": 2,           # 椭圆
    "circle": 2,            # 圆
    "rectangle": 3,         # 矩形
    "square": 3,            # 正方形
    "rounded_rectangle": 4, # 圆角矩形
    "polygon": 5,           # 多边形
}


# ============================================
# 图层管理配置模块
# ============================================

# 添加图层按钮位置（屏幕坐标）
ADD_LAYER_BUTTON_POSITION = (1830, 260)

# 图层视图参数配置
LAYER_VIEW_HEIGHT = 100         # 单个图层视图的高度（像素）
FIRST_LAYER_VIEW_POSITION = (  
    ADD_LAYER_BUTTON_POSITION[0],
    ADD_LAYER_BUTTON_POSITION[1] + LAYER_VIEW_HEIGHT
)                               # 第一个图层视图的坐标

# 右键菜单参数配置
RIGHT_CLICK_OFFSET = (200, 25)  # 右键菜单相对于点击位置的偏移量
OPTION_BOX_PADDING = 5          # 菜单选项内边距（像素）

# 选项卡高度参数
TAB_HEIGHT = 40  # 选项卡高度（像素）

# 图层操作快捷键映射表（按键次数 = 下方向键按下次数）
TAB_KEY_MAP = {
    "hide": 0,        # 隐藏/显示图层
    "copy": 1,        # 复制图层
    "merge_down": 2,  # 向下合并图层
    "move_up": 3,     # 上移图层
    "move_down": 4,   # 下移图层
    "delete": 5,      # 删除图层
}


# ============================================
# 填充工具配置模块
# ============================================

# 默认填充颜色（黑色）位置（屏幕坐标）
FILL_COLOR_POSITION = (955, 100)

# 填充颜色快捷键映射表（按键次数 = 右方向键按下次数）
FILL_COLOR_KEY_MAP = {
    "black": 0,        # 黑色（初始颜色）
    "gray": 1,         # 灰色
    "darkred": 2,      # 深红色
    "red": 3,          # 红色
    "orange": 4,       # 橙色
    "yellow": 5,       # 黄色
    "green": 6,        # 绿色
    "cyan": 7,         # 青绿
    "blue": 8,         # 靛蓝
    "purple": 9,       # 紫色

    "white": 10,       # 白色
    "lightgray": 11,   # 浅灰色
    "brown": 12,       # 褐色
    "rose": 13,        # 玫瑰红
    "gold": 14,        # 金色
    "lightyellow": 15, # 浅黄色
    "lime": 16,        # 酸橙色
    "lightcyan": 17,   # 淡青绿色
    "bluegray": 18,    # 蓝灰色
    "lightpurple": 19  # 浅紫色
}

# ============================================
# 快捷键辅助函数模块
# ============================================

def get_shape_panel_presses(shape: str) -> int:
    """
    获取选择指定形状工具所需的右方向键次数
    若形状不在预设列表中返回-1
    
    :param shape: 形状名称（参考SHAPE_PANEL_KEY_MAP键名）
    :return: 右方向键按下次数（不存在返回-1）
    """
    return SHAPE_PANEL_KEY_MAP.get(shape, -1)

def get_tab_key_presses(operation: str) -> int:
    """
    获取执行图层操作所需的下方向键次数
    若操作不在预设列表中返回-1
    
    :param operation: 图层操作名称（参考TAB_KEY_MAP键名）
    :return: 下方向键按下次数（不存在返回-1）
    """
    return TAB_KEY_MAP.get(operation, -1)

def get_fill_color_presses(color: str) -> int:
    """
    获取选择填充颜色所需的右方向键次数
    若颜色不在预设列表中返回-1
    
    :param color: 颜色名称（参考FILL_COLOR_KEY_MAP键名）
    :return: 右方向键按下次数（不存在返回-1）
    """
    return FILL_COLOR_KEY_MAP.get(color, -1)