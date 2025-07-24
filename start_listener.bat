@echo off
echo 设置PYTHONPATH环境变量...
set PYTHONPATH=%PYTHONPATH%;E:\sad\ThePainter

echo 启动画图动作转录工具...
python .\src\main\python\transcriber\listener.py -a record

echo 程序已退出
pause
