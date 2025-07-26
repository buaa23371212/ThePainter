import re
import ast  # 新增ast模块导入

from src.main.python.terminal_logger.logger import debug

def parse_config_file(path):
    """
    从指定路径的配置文件中解析配置项
    
    Args:
        path: 配置文件路径
        
    Returns:
        dict: 解析后的配置项字典，键为配置名，值为转换后的配置值
    """
    configs = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 提取配置值的正则表达式
        pattern = r"^(\w+)\s*=\s*(.+)$"
        
        for line in content.split("\n"):
            match = re.match(pattern, line.strip())
            if match:
                key, value_str = match.groups()
                try:
                    # 使用ast.literal_eval安全解析值
                    value = ast.literal_eval(value_str)
                    configs[key] = value
                except (ValueError, SyntaxError):
                    # 解析失败时保留原始字符串（去掉首尾空格）
                    configs[key] = value_str.strip()
    except FileNotFoundError:
        # 文件不存在时返回空字典
        pass
    return configs

def replace_lines(lines: list, base_configs: dict) -> list:
    debug(True, lines)
    debug(True, base_configs)

    # 替换配置值，保留注释和格式
    new_lines = []
    for line in lines:
        stripped = line.strip()
        replaced = False
        
        # 检查是否是配置行
        for key, value in base_configs.items():
            # 更精确的匹配：配置名 + 等号
            if re.match(rf"^{key}\s*=", stripped):
                # 使用repr保持类型信息
                formatted_value = repr(value)
                
                # 保留注释部分
                if '#' in line:
                    prefix, comment = line.split('#', 1)
                    new_line = f"{key} = {formatted_value}  #{comment}"
                else:
                    new_line = f"{key} = {formatted_value}\n"
                
                new_lines.append(new_line)
                replaced = True
                break
        
        if not replaced:
            new_lines.append(line)

    debug(True, new_lines)
    
    return new_lines