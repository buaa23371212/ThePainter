from PyQt5.QtWidgets import (
    QListWidget, QListWidgetItem
)

from ui.src.utils.style_loader import load_stylesheets

class NavigationBar(QListWidget):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setFixedWidth(120)  # 固定导航栏宽度
        
        # 添加导航项
        for item_text in items:
            self.addItem(QListWidgetItem(item_text))
        
        load_stylesheets(self, "navigate_bar.css")