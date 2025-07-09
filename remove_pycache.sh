#!/bin/bash

# 查找当前目录下所有的 __pycache__ 文件夹
find . -type d -name "__pycache__" | while read -r folder; do
    # 打印正在删除的文件夹路径
    echo "Deleting $folder"
    # 删除文件夹及其内容
    rm -rf "$folder"
done

echo "All __pycache__ folders have been deleted."