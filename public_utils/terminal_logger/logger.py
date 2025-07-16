import inspect
import os

"""
Logger Module
-------------
提供分级日志输出功能，包含INFO/WARN/ERROR三个等级。
可通过show参数控制日志是否实际输出，show_caller参数控制是否显示调用文件名。
"""

# ANSI颜色转义码
COLOR_RESET = "\033[0m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"  # INFO使用绿色
COLOR_BLUE = "\033[94m"   # DEBUG使用蓝色

# ============================================
# 内部接口 (Internal APIs)
# ============================================

def log(label: str, show: bool, message: str, source_file: str = None, color: str = None) -> None:
    """
    日志记录核心函数
    
    Step:
    1. 检查show标志，如果为False则直接返回
    2. 根据是否提供source_file参数决定输出格式
    3. 应用颜色编码
    4. 将格式化后的日志输出到控制台
    
    :param label: 日志级别标签（如'INFO', 'WARN'等）
    :param show: 是否实际输出日志的标志
    :param message: 需要记录的日志信息
    :param source_file: 日志来源文件名（可选）
    """
    # Step 1: 检查日志输出标志
    if not show:
        return
    
    # Step 2: 格式化日志输出
    if source_file is None:
        log_output = f"[{label}] {message}"
    else:
        log_output = f"[{label}] ({source_file}) {message}"

    # Step 3: 应用颜色编码
    if color:
        log_output = f"{color}{log_output}{COLOR_RESET}"

    # Step 4: 输出到控制台
    print(log_output)


# ============================================
# 外部接口 (Public APIs)
# ============================================

def info(show: bool, message: str, show_caller: bool = False) -> None:
    """
    记录INFO级别日志
    
    Step:
    1. 根据show_caller参数决定是否获取调用文件名
    2. 调用log函数并传入'INFO'标签
    
    :param show: 是否实际输出日志的标志
    :param message: 需要记录的日志信息
    :param show_caller: 是否显示调用文件名（默认为False）
    """
    # Step 1: 决定是否获取调用文件名
    source_file = None
    if show_caller:
        # 使用inspect模块获取调用栈信息
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        # 只保留文件名，去除路径
        source_file = os.path.basename(caller_file)
    
    # Step 2: 调用核心日志函数
    log("INFO", show, message, source_file, COLOR_GREEN)

def warn(show: bool, message: str, show_caller: bool = False) -> None:
    """
    记录WARN级别日志
    
    Step:
    1. 根据show_caller参数决定是否获取调用文件名
    2. 调用log函数并传入'WARN'标签
    
    :param show: 是否实际输出日志的标志
    :param message: 需要记录的日志信息
    :param show_caller: 是否显示调用文件名（默认为False）
    """
    # Step 1: 决定是否获取调用文件名
    source_file = None
    if show_caller:
        # 使用inspect模块获取调用栈信息
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        # 只保留文件名，去除路径
        source_file = os.path.basename(caller_file)
    
    # Step 2: 调用核心日志函数
    log("WARN", show, message, source_file, COLOR_YELLOW)

def error(show: bool, message: str, show_caller: bool = False) -> None:
    """
    记录ERROR级别日志
    
    Step:
    1. 根据show_caller参数决定是否获取调用文件名
    2. 调用log函数并传入'ERROR'标签
    
    :param show: 是否实际输出日志的标志
    :param message: 需要记录的日志信息
    :param show_caller: 是否显示调用文件名（默认为False）
    """
    # Step 1: 决定是否获取调用文件名
    source_file = None
    if show_caller:
        # 使用inspect模块获取调用栈信息
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        # 只保留文件名，去除路径
        source_file = os.path.basename(caller_file)
    
    # Step 2: 调用核心日志函数
    log("ERROR", show, message, source_file, COLOR_RED)

def debug(show: bool, message: str, show_caller: bool = False) -> None:
    """
    记录DEBUG级别日志

    Step:
    1. 根据show_caller参数决定是否获取调用文件名
    2. 调用log函数并传入'DEBUG'标签

    :param show: 是否实际输出日志的标志
    :param message: 需要记录的日志信息
    :param show_caller: 是否显示调用文件名（默认为False）
    """
    source_file = None
    if show_caller:
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        source_file = os.path.basename(caller_file)
    log("DEBUG", True, message, source_file, COLOR_BLUE)