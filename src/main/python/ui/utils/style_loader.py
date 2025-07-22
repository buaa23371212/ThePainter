import os

from src.main.python.terminal_logger.logger import info, warn, error

from src.main.python.configs import project_config


def load_stylesheets(widget, *style_files):
    """
    加载并应用多个样式表文件到指定控件
    
    参数:
        widget: 要应用样式的 Qt 控件
        *style_files: 一个或多个样式表文件名
    """
    try:
        css_dir = project_config.css_dir
        combined_stylesheet = ""
        
        # 加载所有指定的样式表文件
        for style_file in style_files:
            css_path = os.path.join(css_dir, style_file)
            
            if os.path.exists(css_path):
                with open(css_path, "r", encoding="utf-8") as f:
                    combined_stylesheet += f.read() + "\n"
                info(False, f"已加载样式表: {style_file}", True)
            else:
                warn(True, f"样式表文件不存在: {css_path}", True)
        
        # 应用合并后的样式表
        if combined_stylesheet:
            widget.setStyleSheet(combined_stylesheet)
            return True
        else:
            warn(True, "未加载任何样式表", True)
            return False
            
    except Exception as e:
        error(True, f"加载样式表失败: {str(e)}", True)
        return False