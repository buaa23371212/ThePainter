from src.main.python.configs.drawer_panel_config import SHAPE_PANEL_KEY_MAP, FILL_COLOR_KEY_MAP
from src.main.python.transcriber.utils.button_manager import ButtonManager
from src.main.python.transcriber.utils.button_recorder import ButtonRecorder
from src.main.python.terminal_logger.logger import debug

# 创建按钮管理器
manager = ButtonManager()

# 画布区域
canvas_area = ButtonRecorder("Canvas", 280, 910, 310, 1440)
canvas_area.set_tolerance(10)
manager.add_button(canvas_area)

# 取消选中区域
cancel_area = ButtonRecorder("Canvas", 217, 973, 0, 1920)

# ====================================================
# 添加窗口控制按钮
# ====================================================
window_buttons = [
    ButtonRecorder("WinTaskbar", top=1020, bottom=1080, left=0, right=1920),
    ButtonRecorder("WindowMinimization", top=0, bottom=25, left=1740, right=1799),
    ButtonRecorder("WindowClose", top=0, bottom=25, left=1860, right=1920),
    ButtonRecorder("Undo", 35, 74, 383, 422,),
    ButtonRecorder("Redo", 35, 74, 333, 372,)
]
manager.add_buttons(window_buttons)

# ====================================================
# 公共方法：创建工具栏按钮
# ====================================================
def create_toolbar_buttons(
        button_map: dict,
        prefix: str,
        first_button_left: int,
        button_width: int,
        button_height: int,
        button_top: int,
        button_spacing: int,
        start_index: int = 0,  # 新增：起始索引
        item_count: int = None  # 新增：要创建的项目数量
) -> list:
    """
    创建工具栏按钮列表

    参数:
    button_map: 按钮映射字典
    prefix: 按钮名称前缀
    first_button_left: 第一个按钮的左边界
    button_width: 按钮宽度
    button_height: 按钮高度
    button_top: 按钮的顶部Y坐标
    button_spacing: 按钮之间的水平间距
    start_index: 起始索引(默认为0)
    item_count: 要创建的项目数量(None表示全部)

    返回:
    按钮对象列表
    """
    buttons = []
    tolerance = int(button_spacing / 2)  # 转换为整数

    # 按索引值排序字典项
    sorted_items = sorted(button_map.items(), key=lambda x: x[1])

    # 确定要处理的项范围
    if item_count is None:
        items = sorted_items
    else:
        # 确保范围有效
        start = max(0, min(start_index, len(sorted_items) - 1))
        end = min(start + item_count, len(sorted_items))
        items = sorted_items[start:end]

    for item_name, index in items:
        left = first_button_left + (index - start_index) * (button_width + button_spacing)
        right = left + button_width

        # 创建按钮
        btn = ButtonRecorder(
            name=f"{prefix}_{item_name}",
            top=button_top,
            bottom=button_top + button_height,
            left=left,
            right=right
        )
        btn.set_tolerance(tolerance)
        buttons.append(btn)

    return buttons

# ====================================================
# 添加形状工具按钮
# ====================================================
# 形状按钮参数
SHAPE_BUTTON_WIDTH = 18     # 按钮宽度
SHAPE_BUTTON_HEIGHT = 20    # 按钮高度
SHAPE_BUTTON_TOP = 95       # 所有形状按钮的顶部Y坐标
SHAPE_BUTTON_SPACING = 10   # 按钮之间的水平间距

# 第一个形状按钮的位置（直线按钮）
first_shape_button_left = 540

# 创建形状按钮并添加到管理器
shape_buttons = create_toolbar_buttons(
    button_map=SHAPE_PANEL_KEY_MAP,
    prefix="Shape",
    first_button_left=first_shape_button_left,
    button_width=SHAPE_BUTTON_WIDTH,
    button_height=SHAPE_BUTTON_HEIGHT,
    button_top=SHAPE_BUTTON_TOP,
    button_spacing=SHAPE_BUTTON_SPACING,
    item_count=9
)
manager.add_buttons(shape_buttons)

# ====================================================
# 添加颜色选择按钮
# ====================================================
# 颜色按钮参数
COLOR_BUTTON_WIDTH = 18     # 按钮宽度
COLOR_BUTTON_HEIGHT = 20    # 按钮高度
COLOR_BUTTON_TOP = 95       # 按钮的顶部Y坐标
COLOR_BUTTON_SPACING = 12   # 按钮之间的水平间距

# 第一个颜色按钮的位置
first_color_button_left = 951

# 创建颜色按钮并添加到管理器
color_buttons = create_toolbar_buttons(
    button_map=FILL_COLOR_KEY_MAP,
    prefix="Color",
    first_button_left=first_color_button_left,
    button_width=COLOR_BUTTON_WIDTH,
    button_height=COLOR_BUTTON_HEIGHT,
    button_top=COLOR_BUTTON_TOP,
    button_spacing=COLOR_BUTTON_SPACING,
    start_index=0,
    item_count=10
)

COLOR_BUTTON_TOP_2 = 120

color_buttons_2 = create_toolbar_buttons(
    button_map=FILL_COLOR_KEY_MAP,
    prefix="Color",
    first_button_left=first_color_button_left,
    button_width=COLOR_BUTTON_WIDTH,
    button_height=COLOR_BUTTON_HEIGHT,
    button_top=COLOR_BUTTON_TOP_2,
    button_spacing=COLOR_BUTTON_SPACING,
    start_index=10,
    item_count=10
)

manager.add_buttons(color_buttons)
manager.add_buttons(color_buttons_2)

# ====================================================
# 添加其他重要按钮
# ====================================================
# 填充工具按钮
fill_tool_btn = ButtonRecorder(
    name="Tool_fill",
    top=91,
    bottom=131,
    left=345,
    right=384
)
manager.add_button(fill_tool_btn)

# 文本工具按钮
text_tool_btn = ButtonRecorder(
    name="Tool_text",
    top=91,
    bottom=131,
    left=395,
    right=434
)
manager.add_button(text_tool_btn)

# 图层工具按钮
layer_tool_btn = ButtonRecorder(
    name="Tool_layer",
    top=112,
    bottom=158,
    left=1419,
    right=1467
)
manager.add_button(layer_tool_btn)

# 添加图层按钮
add_layer_btn = ButtonRecorder(
    name="AddLayer",
    top=249,
    bottom=276,
    left=1821,
    right=1848
)
manager.add_button(add_layer_btn)