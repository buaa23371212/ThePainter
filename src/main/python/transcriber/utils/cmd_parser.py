import argparse

from src.main.python.transcriber import ACTION_CHOICE
from src.main.python.transcriber.utils import DEFAULT_FILE_PATH

def parse_arguments(args=None):
    """解析命令行参数并返回结果"""
    parser = argparse.ArgumentParser(
        description="Mouse Event Recorder and Processor",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-a', '--action',
        choices=ACTION_CHOICE,
        default='record',
        help="""
选择要执行的操作：
  record          : 记录并打印鼠标事件（默认）
  export          : 记录并导出到文件
  convert         : 记录并转换为绘图命令
  full            : 记录、转换并打印绘图命令
  parse           : 从文件解析并转换为绘图命令
  parse_and_save  : 从文件解析、转换并保存绘图命令
        """
    )
    parser.add_argument(
        '-f', '--file',
        default=DEFAULT_FILE_PATH,
        help=f"指定鼠标事件输入/输出文件路径（默认：{DEFAULT_FILE_PATH}）"
    )
    parser.add_argument(
        '-c', '--command-file',
        help="指定绘图命令输出文件路径（仅对parse_and_save操作有效）"
    )
    parser.add_argument(
        '-p', '--print-commands',
        action='store_true',
        help="在转换后打印绘图命令（仅对convert/parse操作有效）"
    )

    return parser.parse_args(args)