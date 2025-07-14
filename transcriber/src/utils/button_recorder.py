class ButtonRecorder:
    def __init__(self, name: str, top: int, bottom: int, left: int, right: int):
        """
        初始化按钮记录器

        参数:
        name: 按钮名称
        top: 上边界Y坐标
        bottom: 下边界Y坐标
        left: 左边界X坐标
        right: 右边界X坐标
        """
        # 验证边界有效性
        if top >= bottom:
            raise ValueError("上边界必须小于下边界")
        if left >= right:
            raise ValueError("左边界必须小于右边界")

        self.name = name
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.tolerance = 0  # 默认容忍值为0

    @property
    def width(self) -> int:
        """计算按钮宽度"""
        return self.right - self.left

    @property
    def height(self) -> int:
        """计算按钮高度"""
        return self.bottom - self.top

    @property
    def area(self) -> int:
        """计算按钮区域面积"""
        return self.width * self.height

    @property
    def center(self) -> tuple:
        """获取中心点坐标"""
        center_x = (self.left + self.right) // 2
        center_y = (self.top + self.bottom) // 2
        return (center_x, center_y)

    def set_tolerance(self, tolerance: int):
        """
        设置边界容忍值

        参数:
        tolerance: 容忍值(像素数)
        """
        if tolerance < 0:
            raise ValueError("容忍值不能为负数")
        self.tolerance = tolerance

    def contains_point(self, x: int, y: int, tolerance: int = None) -> bool:
        """
        检查点是否在按钮区域内(考虑容忍值)

        参数:
        x: 点的X坐标
        y: 点的Y坐标
        tolerance: 可选的自定义容忍值(覆盖类级别的容忍值)

        返回:
        bool - 点是否在区域内
        """
        # 使用自定义容忍值(如果提供)，否则使用类级别的容忍值
        use_tolerance = self.tolerance if tolerance is None else tolerance

        return (self.left - use_tolerance <= x <= self.right + use_tolerance) and \
            (self.top - use_tolerance <= y <= self.bottom + use_tolerance)

    def to_dict(self) -> dict:
        """将按钮信息转换为字典"""
        return {
            'name': self.name,
            'top': self.top,
            'bottom': self.bottom,
            'left': self.left,
            'right': self.right,
            'width': self.width,
            'height': self.height,
            'area': self.area,
            'center_x': self.center[0],
            'center_y': self.center[1],
            'tolerance': self.tolerance
        }

    def __repr__(self) -> str:
        """返回对象的正式字符串表示"""
        return (f"ButtonRecorder(name='{self.name}', "
                f"top={self.top}, bottom={self.bottom}, "
                f"left={self.left}, right={self.right}, "
                f"tolerance={self.tolerance})")

    def __str__(self) -> str:
        """返回对象的友好字符串表示"""
        return (f"Button '{self.name}': "
                f"Position[{self.left},{self.top}]-[{self.right},{self.bottom}], "
                f"Size={self.width}x{self.height}, "
                f"Tolerance={self.tolerance}px")