import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QStackedWidget
)

from src.main.python.ui.fragments.ai_page import AIPage
from src.main.python.ui.fragments.explorer_page import FileExplorer
from src.main.python.ui.fragments.listener_page import ListenerPage
from src.main.python.ui.fragments.output_box import OutputDisplay
from src.main.python.ui.fragments.paintings_page import PaintingsPage
from src.main.python.ui.fragments.settings_page import SettingsPage
from src.main.python.ui.fragments.navigate_bar import NavigationBar
from src.main.python.ui.utils.style_loader import load_stylesheets

class MainWindow(QWidget):
    def __init__(self):
        """
        MainWindow Structure:
             ├── NavigationBar (左侧导航栏)
             └── right_container (右侧容器)
                    ├── stack (堆叠组件，包含5个页面)
                    |     ├── FileExplorer (0)
                    |     ├── ListenerPage (1)
                    |     ├── PaintingsPage (2)
                    |     ├── AIPage (3)
                    |     └── SettingsPage (4)
                    └── OutputDisplay (输出显示栏)
        """
        super().__init__()

        # ====================================================================
        # STEP 1: 初始化主窗口基础设置
        # ====================================================================
        self.setWindowTitle("ThePainter")               # 窗口标题
        self.resize(800, 500)                           # 初始窗口尺寸

        # ====================================================================
        # STEP 2: 创建主布局框架（水平布局）
        # ====================================================================
        main_layout = QHBoxLayout(self)                 # 水平布局：左侧导航 + 右侧内容区
        main_layout.setContentsMargins(0, 0, 0, 0)      # 移除布局边距

        # ====================================================================
        # STEP 3: 创建并添加导航栏（左侧功能区）
        # ====================================================================
        nav_items = ["资源管理器", "屏幕监听器", "画作列表", "AI作画", "设置"]
        self.nav_list = NavigationBar(nav_items, 120)    # 创建导航栏实例
        main_layout.addWidget(self.nav_list)             # 添加到主布局左侧

        # ====================================================================
        # STEP 4: 创建右侧内容容器（垂直布局）
        # ====================================================================
        self.right_container = QWidget()
        self.right_layout = QVBoxLayout(self.right_container)
        self.right_layout.setContentsMargins(0, 0, 0, 0)  # 移除内边距
        self.right_layout.setSpacing(0)                   # 移除组件间距

        # ====================================================================
        # STEP 5: 创建页面堆叠组件（多页面容器）
        # ====================================================================
        self.stack = QStackedWidget()  # 多页面切换容器

        # --------------------------------------------------
        # STEP 5.1: 添加文件资源管理器页面
        # --------------------------------------------------
        self.file_explorer = FileExplorer()
        self.stack.addWidget(self.file_explorer)  # 索引0

        # --------------------------------------------------
        # STEP 5.2: 添加屏幕监听器页面
        # --------------------------------------------------
        self.listener = ListenerPage()
        self.stack.addWidget(self.listener)        # 索引1

        # --------------------------------------------------
        # STEP 5.3: 添加画作列表页面
        # --------------------------------------------------
        self.paintings_page = PaintingsPage()
        self.stack.addWidget(self.paintings_page) # 索引2

        # --------------------------------------------------
        # STEP 5.4: 添加AI作画页面
        # --------------------------------------------------
        self.ai_page = AIPage()
        self.ai_page.input_box.setText("生成一幅简笔画")  # 默认提示文本
        self.stack.addWidget(self.ai_page)         # 索引3

        # --------------------------------------------------
        # STEP 5.5: 添加设置页面
        # --------------------------------------------------
        self.setting_page = SettingsPage()
        self.stack.addWidget(self.setting_page)    # 索引4

        self.listener.set_setting_page(self.setting_page.get_other_setting_page())

        self.right_layout.addWidget(self.stack)    # 将堆叠组件添加到右侧布局

        # ====================================================================
        # STEP 6: 创建并添加输出显示栏
        # ====================================================================
        self.text_view = OutputDisplay()

        # 为需要输出的页面设置输出视图
        self.file_explorer.set_output_view(self.text_view)
        self.listener.set_output_view(self.text_view)

        self.right_layout.addWidget(self.text_view)  # 添加到右侧布局底部

        # ====================================================================
        # STEP 7: 完成主布局组装
        # ====================================================================
        main_layout.addWidget(self.right_container)  # 将右侧容器添加到主布局

        # ====================================================================
        # STEP 8: 连接导航栏与页面切换功能
        # ====================================================================
        # 绑定导航栏点击事件：切换堆叠页面
        self.nav_list.currentRowChanged.connect(self.stack.setCurrentIndex)
        # 默认选中第一项（资源管理器）
        self.nav_list.setCurrentRow(0)

        # ====================================================================
        # STEP 9: 加载并应用样式表
        # ====================================================================
        load_stylesheets(self,
                         "container.css", "button.css", "list.css",
                         "scroll_bar.css", "splitter.css",
                         "text_edit.css", "title.css", "tree.css")

# TODO
flags = {
    'debug': False
}


if __name__ == "__main__":
    # ====================================================================
    # STEP 10: 启动应用程序
    # ====================================================================
    app = QApplication(sys.argv)            # 创建Qt应用
    window = MainWindow()                   # 实例化主窗口
    window.show()                           # 显示窗口
    sys.exit(app.exec_())                   # 启动应用事件循环