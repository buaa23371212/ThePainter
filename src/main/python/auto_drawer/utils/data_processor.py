import os
import json

from src.main.python.configs.project_config import get_project_root

def load_shape_from_json(file_path, shape_type, shape_id=None, shape_name=None):
    """
    从JSON文件加载形状的点数据

    Step:
    1. 打开并读取JSON文件
    2. 解析JSON数据
    3. 根据ID或名称查找形状
    4. 返回点列表

    参数:
        file_path (str): JSON文件路径
        shape_type (str): 形状类型，如 "curves" 或 "polygons"
        shape_id (str): 形状的ID标识符
        shape_name (str): 形状的名称

    返回:
        list: 形状点列表 [(x0, y0), (x1, y1), ...]
    """
    project_root = get_project_root()
    # 拼接项目根目录和相对路径
    full_file_path = os.path.join(project_root, file_path)

    try:
        # Step 1: 打开文件
        with open(full_file_path, 'r') as f:
            data = json.load(f)

        # Step 2: 获取形状数据
        shapes = data.get(shape_type, {})

        # Step 3: 根据ID或名称查找
        if shape_id and shape_id in shapes:
            return shapes[shape_id].get('points', [])

        if shape_name:
            for s_id, s_data in shapes.items():
                if s_data.get('name') == shape_name:
                    return s_data.get('points', [])

        # 未找到形状
        raise ValueError(f"在文件 {file_path} 中未找到指定形状: id={shape_id}, name={shape_name}, type={shape_type}")

    except FileNotFoundError:
        raise FileNotFoundError(f"JSON文件未找到: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"无效的JSON格式: {file_path}")


def convert_points_to_coords(points):
    """
    将点整数列表转换为坐标元组列表

    前置条件
    - 确保验证过点的合法性

    Step:
    1. 每两个整数组成一个点
    2. 返回点元组列表

    参数:
        points (list of int): 点坐标列表 [x0, y0, x1, y1, x2, y2, x3, y3]

    返回:
        list: 点元组列表 [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
    """
    # Step 1: 转换格式
    coords = []
    for i in range(0, len(points), 2):
        x = points[i]
        y = points[i+1]
        coords.append((x, y))

    return coords

def validate_shape_args(args):
    """
    验证参数的有效性

    Step:
    1. 验证文件方式参数
    2. 验证顶点方式参数
    3. 确保参数组合有效

    参数:
        args: 命令行参数对象
    """
    # Step 1: 验证文件方式参数
    if args.file:
        if not (args.id or args.name):
            raise ValueError("使用文件时，必须提供-id或-name参数")
        if args.id and args.name:
            raise ValueError("不能同时使用-id和-name参数")

    # Step 2: 验证顶点方式参数
    # TODO: 需要统一
    elif args.points:
        if len(args.points) % 2 != 0:
            raise ValueError("顶点坐标数量必须为偶数")
        if args.id or args.name:
            raise ValueError("直接指定顶点时，不能使用-id或-name参数")