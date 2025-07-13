import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QStackedWidget,
    QTextEdit
)

from ui.fragments.ai_page import AIPage
from ui.fragments.explorer import FileExplorer
from ui.fragments.paintings_page import PaintingsPage
from ui.fragments.settings_page import SettingsPage
from ui.fragments.navigate_bar import NavigationBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 主窗口基础设置
        self.setWindowTitle("ThePainter")               # 窗口标题
        self.resize(800, 500)                           # 初始窗口尺寸

        # 主布局：水平布局（左侧导航栏 + 右侧内容区）
        main_layout = QHBoxLayout(self)                 # 创建水平布局作为主框架
        main_layout.setContentsMargins(0, 0, 0, 0)      # 可选：移除布局边距

        # ==================================================
        # 左侧导航栏 (功能选择区)
        # ==================================================
        # 定义导航项名称
        nav_items = ["资源管理器", "AI作画", "画作列表", "设置"]
        
        # 创建导航栏实例
        self.nav_list = NavigationBar(nav_items)                  
        main_layout.addWidget(self.nav_list)            # 将导航栏添加到主布局左侧

        # ==================================================
        # 右侧内容区 (多页面容器)
        # ==================================================
        # 创建一个容器控件来容纳右侧布局
        self.right_container = QWidget()
        self.right_layout = QVBoxLayout(self.right_container)
        self.right_layout.setContentsMargins(0, 0, 0, 0)  # 移除内边距
        self.right_layout.setSpacing(0)                   # 移除组件间距

        self.stack = QStackedWidget()                           # 创建堆叠组件实现多页面切换
        
        # 页面1: 文件资源管理器 (自定义组件)
        self.file_explorer = FileExplorer()                     # 实例化文件管理器
        self.stack.addWidget(self.file_explorer)                # 添加到堆叠组件
        
        # 页面2: AI作画
        self.ai_page = AIPage()
        self.ai_page.input_box.setText("生成一幅简笔画")        # 模拟输入
        self.stack.addWidget(self.ai_page)

        # 页面3: 
        self.paintings_page = PaintingsPage()
        self.stack.addWidget(self.paintings_page)

        # 页面4:
        self.setting_page = SettingsPage()
        self.stack.addWidget(self.setting_page)

        # 后续可扩展更多页面，例如：
        # self.canvas_page = CanvasPage()
        # self.stack.addWidget(self.canvas_page)
        
        self.right_layout.addWidget(self.stack)

        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        self.text_view.setVisible(False)

        self.right_layout.addWidget(self.text_view)

        main_layout.addWidget(self.right_container)      # 将容器控件添加到主布局右侧

        # ==================================================
        # 功能连接：导航栏切换控制内容区显示
        # ==================================================
        # 绑定导航栏点击事件：当前行变化时切换堆叠页面
        self.nav_list.currentRowChanged.connect(self.stack.setCurrentIndex)
        # 默认选中第一项（资源管理器）
        self.nav_list.setCurrentRow(0)  

if __name__ == "__main__":
    app = QApplication(sys.argv)            # 创建Qt应用
    window = MainWindow()                   # 实例化主窗口
    window.show()                           # 显示窗口
    sys.exit(app.exec_())                   # 启动应用事件循环