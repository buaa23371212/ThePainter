@echo off
echo 设置PYTHONPATH环境变量...
set PYTHONPATH=%PYTHONPATH%;E:\sad\ThePainter

echo 启动绘画工具UI...
set PYTHON_EXE=.\.venv\Scripts\python.exe
%PYTHON_EXE% .\src\main\python\ui\painter_ui.py

echo 程序已退出
pause
