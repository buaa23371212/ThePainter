from typing import List, Dict, Optional

from src.main.python.transcriber.utils.button_recorder import ButtonRecorder

class ButtonManager:
    def __init__(self):
        """按钮管理器，用于高效处理按钮点击检测"""
        self.buttons: List[ButtonRecorder] = []  # 存储所有按钮
        self.button_grid: Dict[tuple, List[ButtonRecorder]] = {}  # 空间分割网格
        self.grid_size = 100  # 网格大小，根据实际情况调整
        self.grid_initialized = False  # 网格是否已初始化

    def add_button(self, button: ButtonRecorder):
        """添加一个按钮"""
        self.buttons.append(button)
        self.grid_initialized = False  # 添加按钮后需要重新初始化网格

    def add_buttons(self, buttons: List[ButtonRecorder]):
        """批量添加按钮"""
        self.buttons.extend(buttons)
        self.grid_initialized = False

    def remove_button(self, name: str):
        """根据名称移除按钮"""
        self.buttons = [btn for btn in self.buttons if btn.name != name]
        self.grid_initialized = False

    def _initialize_grid(self):
        """初始化空间分割网格"""
        self.button_grid = {}

        # 计算所有按钮的最小最大坐标
        if not self.buttons:
            return

        min_x = min(btn.left for btn in self.buttons)
        max_x = max(btn.right for btn in self.buttons)
        min_y = min(btn.top for btn in self.buttons)
        max_y = max(btn.bottom for btn in self.buttons)

        # 创建网格
        for btn in self.buttons:
            # 计算按钮所属的网格区域
            start_col = max(min_x, btn.left) // self.grid_size
            end_col = max_x // self.grid_size if btn.right >= max_x else btn.right // self.grid_size
            start_row = max(min_y, btn.top) // self.grid_size
            end_row = max_y // self.grid_size if btn.bottom >= max_y else btn.bottom // self.grid_size

            # 将按钮添加到覆盖的所有网格中
            for col in range(start_col, end_col + 1):
                for row in range(start_row, end_row + 1):
                    grid_key = (col, row)
                    if grid_key not in self.button_grid:
                        self.button_grid[grid_key] = []
                    self.button_grid[grid_key].append(btn)

        self.grid_initialized = True

    def find_button_at_point(self, x: int, y: int, method: str = "grid") -> Optional[ButtonRecorder]:
        """
        查找给定点所在的按钮

        参数:
        x, y: 点击坐标
        method: 搜索方法 ('enum', 'grid', 'smallest', 'largest')

        返回:
        找到的按钮对象，如果没找到则返回None
        """
        if not self.buttons:
            return None

        # 方法1: 简单枚举法（适用于按钮数量少的情况）
        if method == "enum":
            for btn in reversed(self.buttons):  # 从后往前，后添加的按钮优先
                if btn.contains_point(x, y):
                    return btn
            return None

        # 确保网格已初始化
        if not self.grid_initialized:
            self._initialize_grid()

        # 方法2: 使用空间网格加速
        if method == "grid":
            # 计算点所在的网格
            grid_key = (x // self.grid_size, y // self.grid_size)

            # 检查该网格和相邻网格（处理跨越网格边界的按钮）
            candidates = []
            for col_offset in (-1, 0, 1):
                for row_offset in (-1, 0, 1):
                    neighbor_key = (grid_key[0] + col_offset, grid_key[1] + row_offset)
                    if neighbor_key in self.button_grid:
                        candidates.extend(self.button_grid[neighbor_key])

            # 去重并检查候选按钮
            for btn in set(candidates):
                if btn.contains_point(x, y):
                    return btn
            return None

        # 方法3: 返回面积最小的按钮（适用于重叠区域）
        if method == "smallest":
            smallest_btn = None
            smallest_area = float('inf')

            for btn in self.buttons:
                if btn.contains_point(x, y) and btn.area < smallest_area:
                    smallest_btn = btn
                    smallest_area = btn.area
            return smallest_btn

        # 方法4: 返回面积最大的按钮
        if method == "largest":
            largest_btn = None
            largest_area = 0

            for btn in self.buttons:
                if btn.contains_point(x, y) and btn.area > largest_area:
                    largest_btn = btn
                    largest_area = btn.area
            return largest_btn

        raise ValueError(f"未知的搜索方法: {method}")

    def get_button_by_name(self, name: str) -> Optional[ButtonRecorder]:
        """根据名称获取按钮"""
        for btn in self.buttons:
            if btn.name == name:
                return btn
        return None

    def clear_all_buttons(self):
        """清除所有按钮"""
        self.buttons = []
        self.button_grid = {}
        self.grid_initialized = False