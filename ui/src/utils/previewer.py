import re
from auto_drawer.src.utils.command_executor import _extract_comment_words
from public_utils.terminal_logger.command_logger import title, step

def preview_command_file(input_file_path):
    """
    只预览命令文件中的标题和步骤说明，不执行命令
    """
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # 标题块处理 (三行格式)
            if line.startswith("# =") and i + 2 < len(lines):
                title_line = lines[i + 1].strip()
                end_line = lines[i + 2].strip()
                if end_line.startswith("# ="):
                    title(True, _extract_comment_words(title_line), False)
                    i += 3
                    continue
                else:
                    i += 1
                    continue

            # 步骤说明处理
            if line.startswith("# "):
                comment = _extract_comment_words(line)
                if comment and re.match(r"^\d+\.\s", comment):
                    step(True, comment, False)
                elif comment:
                    step(False, comment, False)
                i += 1
                continue

            i += 1