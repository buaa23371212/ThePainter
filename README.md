# ThePainter (自动化绘图工具)

## 项目概述
ThePainter 是一个基于Python的自动化绘图工具，能够解析用户指令并自动执行绘图操作。它由三个主要组件构成：
- **auto_drawer**：负责解析用户指令并执行自动化绘图操作
- **transcriber**：将用户操作转录为结构化命令
- **ui**：提供用户界面（具体结构见文档）

## 安装指南

### 系统要求
- Python 3.7+
- Windows 系统（依赖系统自带的画图工具）

### 安装步骤
```bash
# 克隆项目仓库
git clone https://github.com/buaa23371212/ThePainter.git
cd ThePainter

# 安装依赖
pip install -r requirements.txt
```

### 依赖包
```text
PyQt5~=5.15.11
PyAutoGUI~=0.9.54
pynput~=1.8.1
```

## 使用说明

### 基本工作流程
1. 命令行执行`./start_painter.bat`进入 ui 界面
2. 左侧导航栏是导航栏，可以选择不同的功能
3. `资源管理器`：可以查看`input`目录下的指令与`output`目录下的对应的图片
4. `屏幕监听器`：有开始按钮，点击后进入监听模式，可以将在画图工具的操作转化为`auto_drawer`模块可以执行的命令文件
5. `画作列表`：可以查看图画内容与对应的命令代码
6. `AI作画`：待实现
7. 设置界面：可以调节`auto_drawer`的绘画速度，可以调节启动`transcriber`使用的命令参数

## 模块说明

### auto_drawer 模块
#### 1. 命令解析器 (command_parser)
- 功能：给`painter.py`与`command_executor.py`提供命令行参数解析功能
- 示例：`circle -center 600 400 200`，表示在画布上以 (600, 400) 为中心画一个半径 200 的圆

#### 2. command_executor.py
auto_drawer 的核心模块，依赖于其他模块，为`painter.py`提供命令执行功能

#### 3. 画布工具 (canvas_tools.py)
```python
def open_paint():  # 打开画图工具
def minimize_paint():  # 最小化窗口
def click_shapes_button():  # 切换到形状绘制模式
def activate_canvas():  # 激活画布窗口
```

#### 4. 绘图工具 (drawer)
| 图形类型   | 文件               | 功能函数              |
|------------|--------------------|-----------------------|
| 直线       | line_drawer.py     | select_line_tool()    |
| 圆形       | circle_drawer.py   | draw_circle_command() |
| 曲线       | curve_drawer.py    | draw_curve_command()  |

#### 5. 颜色处理 (colorer.py)
```python
choose_color("red")  # 选择红色
select_fill_tool()  # 切换到填充工具
fill_color("blue", x=100, y=100)  # 在指定位置填充蓝色
```

#### 6. 文本输入 (texter.py)
```python
select_texter_tool()  # 切换到文本工具
create_text("Hello", x=50, y=50)  # 在指定位置创建文本
```

#### 7. 图层工具 (layer_tools.py)
```python
add_layer()  # 添加新图层
select_layer(2)  # 选择图层2
select_layer_operation("hide", 3)  # 隐藏图层3
```

#### 8. 图片保存 (png_saver.py)
待实现

#### 9. 配置模块
- `auto_speed_manager.py`：控制鼠标移动速度
- `screen_config.py`：定义画布坐标位置

### transcriber 模块
#### 1. command_generator.py
将鼠标事件转化为命令，并提供命令导出为文件(.pcmd)功能

#### 2. 鼠标事件处理 (mouse_recorder.py)
```python
parse_from_file("events.json")  # 从JSON解析鼠标事件
```

#### 3. 按钮记录器 (button_recorder.py)
```python
button = ButtonRecorder("Save", top=10, bottom=50, left=10, right=50)
button.contains_point(25, 30)  # 检查点是否在按钮内
```

#### 4. 按钮管理器 (button_manager.py)
```python
manager = ButtonManager()
manager.add_button(button)
manager.find_button_at_point(30, 40, method="grid")  # 使用网格搜索按钮
```

### UI 模块
- 用户界面结构详见：[structure.md](ui/structure.md)

## 流程图与指令集
- **auto_drawer流程图**：[流程图.md](auto_drawer/流程图.md)
- **auto_drawer指令集**：[instruction set.md](auto_drawer/instruction%20set.md)
- **transcriber流程图**：[流程图.md](transcriber/流程图.md)
- **transcriber指令集**：[instruction set.md](transcriber/instruction%20set.md)

## 贡献指南
> 待补充：项目贡献规范、代码提交流程和分支管理策略

## 许可证
> 待补充：项目使用的开源许可证信息

## 技术支持
> 待补充: 如有任何问题，请提交issue至项目仓库或联系：......