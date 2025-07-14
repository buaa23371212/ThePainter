from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize

def get_scaled_pixmap(image_path, container_size, min_size=QSize(100, 100)):
    """
    获取缩放后的图片
    
    参数:
        image_path: 图片文件路径
        container_size: 容器尺寸 (QSize)
        min_size: 最小显示尺寸 (默认 100x100)
    
    返回:
        QPixmap: 缩放后的图片对象
        str: 错误信息（成功时返回空字符串）
    """
    if not image_path:
        return None, "无图片路径"
    
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        return None, "图片加载失败"
    
    # 计算缩放尺寸（保持比例）
    scaled_size = pixmap.size().scaled(
        container_size, 
        Qt.KeepAspectRatio
    )
    
    # 确保不小于最小尺寸
    if scaled_size.width() < min_size.width():
        scale_factor = min_size.width() / scaled_size.width()
        scaled_size = QSize(
            min_size.width(),
            int(scaled_size.height() * scale_factor)
        )
    if scaled_size.height() < min_size.height():
        scale_factor = min_size.height() / scaled_size.height()
        scaled_size = QSize(
            int(scaled_size.width() * scale_factor),
            min_size.height()
        )
    
    # 应用缩放
    return pixmap.scaled(
        scaled_size, 
        Qt.KeepAspectRatio, 
        Qt.SmoothTransformation
    ), ""