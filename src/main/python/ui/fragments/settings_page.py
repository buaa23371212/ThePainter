from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QStackedWidget, QLabel
)

from src.main.python.ui.fragments import SETTING_TYPES
from src.main.python.ui.fragments.auto_speed_setting_page import AutoOperationSpeedPage
from src.main.python.ui.fragments.listener_setting_page import ListenerSettingPage
from src.main.python.ui.fragments.navigate_bar import NavigationBar


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        # ====================================================================
        # STEP 1: 初始化主布局
        # ====================================================================
        main_layout = QHBoxLayout(self)  # 水平布局：左侧导航 + 右侧内容区
        main_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距
        main_layout.setSpacing(0)  # 移除组件间距

        # ====================================================================
        # STEP 2: 创建左侧设置类型导航栏
        # ====================================================================
        # 定义设置类型列表
        settings_types = SETTING_TYPES  # 可扩展更多设置类型

        # 创建导航栏实例
        self.settings_list = NavigationBar(settings_types, 150)
        main_layout.addWidget(self.settings_list)  # 添加到布局左侧

        # ====================================================================
        # STEP 3: 创建右侧设置区域（堆叠页面）
        # ====================================================================
        self.settings_stack = QStackedWidget()  # 创建堆叠组件实现多设置页面切换
        main_layout.addWidget(self.settings_stack, stretch=1)  # 添加到布局右侧并占据剩余空间

        # ====================================================================
        # STEP 3.1: 添加自动操作速度设置页面
        # ====================================================================
        self.speed_page = AutoOperationSpeedPage()                          # 创建自动操作速度设置页面
        self.speed_page.confirm_button.clicked.connect(self.save_settings)  # 连接保存事件
        self.settings_stack.addWidget(self.speed_page)                      # 添加到堆叠组件（索引0）

        # ====================================================================
        # STEP 3.2: 添加鼠标动作监听器设置页面（包含print_commands开关）
        # ====================================================================
        self.listener_settings_page = ListenerSettingPage()
        self.settings_stack.addWidget(self.listener_settings_page)     # 将页面添加到堆叠组件（索引1）

        # ====================================================================
        # STEP 4: 连接导航与页面切换功能
        # ====================================================================
        # 绑定导航栏点击事件：切换设置页面
        self.settings_list.currentRowChanged.connect(self.settings_stack.setCurrentIndex)

        # 默认选中第一项（自动操作速度设置）
        self.settings_list.setCurrentRow(0)

    # ========================================================================
    # 设置保存模块
    # ========================================================================
    def save_settings(self):
        """
        保存设置并在终端输出信息
        - 调用自动操作速度页面的保存方法
        """
        self.speed_page.save_settings()  # 调用当前页面的保存方法

    def get_other_setting_page(self):
        return self.listener_settings_page