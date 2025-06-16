import inspect
import os

def log(label: str, show: bool, message: str, source_file: str = None):
    """
    打印带标签的终端输出。

    :param label: 输出标签，如'INFO'、'WARN'等
    :param show: 是否显示输出
    :param message: 输出内容
    :param source_file: 来源文件名（可选，默认自动获取调用者文件名）
    """
    if not show:
        return
    if source_file is None:
        print(f"[{label}] {message}")
    else:
        print(f"[{label}] ({source_file}) {message}")

def info(show: bool, message: str, source_file: str = None):
    log("INFO", show, message, source_file)

def warn(show: bool, message: str, source_file: str = None):
    log("WARN", show, message, source_file)

def error(show: bool, message: str, source_file: str = None):
    log("ERROR", show, message, source_file)