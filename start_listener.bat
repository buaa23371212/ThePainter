@echo off
echo 设置PYTHONPATH环境变量...
set PYTHONPATH=%PYTHONPATH%;E:\sad\ThePainter

echo 启动画图动作转录工具...
set PYTHON_EXE=.\.venv\Scripts\python.exe
%PYTHON_EXE% .\src\main\python\transcriber\listener.py -a parse -f "E:/sad/ThePainter/data/json/mouse_event.json" -p

@REM -a record

echo 程序已退出
pause
