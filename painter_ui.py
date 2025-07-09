import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QStackedWidget, QFileSystemModel, QTreeView
)
from PyQt5.QtCore import Qt, QDir

from ui.explorer import FileExplorer
from ui.ai_page import AIPage
from ui.paintings_page import PaintingsPage

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
        self.nav_list = QListWidget()                           # 创建列表控件作为导航栏
        self.nav_list.setFixedWidth(120)                        # 固定导航栏宽度
        
        # 添加导航项 (可扩展)
        self.nav_list.addItem(QListWidgetItem("资源管理器"))    # 第一个功能入口
        self.nav_list.addItem(QListWidgetItem("AI作画"))        # 第二个功能入口
        self.nav_list.addItem(QListWidgetItem("画作列表"))      # 第三个功能入口
        # 后续可添加更多功能项，例如：
        # self.nav_list.addItem(QListWidgetItem("画板"))
        # self.nav_list.addItem(QListWidgetItem("设置"))
        
        main_layout.addWidget(self.nav_list)                    # 将导航栏添加到主布局左侧

        # ==================================================
        # 右侧内容区 (多页面容器)
        # ==================================================
        self.stack = QStackedWidget()                           # 创建堆叠组件实现多页面切换
        
        # 页面1: 文件资源管理器 (自定义组件)
        self.file_explorer = FileExplorer()                     # 实例化文件管理器
        self.stack.addWidget(self.file_explorer)                # 添加到堆叠组件
        
        # 页面2: AI作画
        self.ai_page = AIPage()
        self.ai_page.input_box.setText("生成一幅简笔画")
        self.stack.addWidget(self.ai_page)    

        # 页面3: 
        self.paintings_page = PaintingsPage()
        self.stack.addWidget(self.paintings_page)

        # 后续可扩展更多页面，例如：
        # self.canvas_page = CanvasPage()
        # self.stack.addWidget(self.canvas_page)
        
        main_layout.addWidget(self.stack)                       # 将堆叠组件添加到主布局右侧

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