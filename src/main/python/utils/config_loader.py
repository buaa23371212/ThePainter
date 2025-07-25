import re


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
                key, value = match.groups()
                try:
                    # 尝试转换为数值类型
                    configs[key] = float(value) if '.' in value else int(value)
                except ValueError:
                    configs[key] = value  # 保留原始字符串（如果转换失败）
    except FileNotFoundError:
        # 文件不存在时返回空字典
        pass
    return configs

def replace_lines(lines: str, base_configs):
    # 替换配置值，保留注释和格式
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 检查是否是配置行
        for key, value in base_configs.items():
            if stripped.startswith(f"{key} ="):
                # 保留注释部分
                if '#' in line:
                    prefix, comment = line.split('#', 1)
                    new_line = f"{key} = {value}  # {comment}"
                else:
                    new_line = f"{key} = {value}\n"
                new_lines.append(new_line)
                break
            else:
                # 不是配置行，保留原样
                new_lines.append(line)

    return new_lines