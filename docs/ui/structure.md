```
MainWindow Structure:
             ├── NavigationBar (左侧导航栏)
             └── right_container (右侧容器，垂直布局)
                    ├── stack (堆叠组件，包含5个页面)
                    |     ├── FileExplorer (0)
                    |     ├── ListenerPage (1)
                    |     ├── PaintingsPage (2)
                    |     ├── AIPage (3)
                    |     └── SettingsPage (4)
                    └── OutputDisplay (输出显示栏，位于堆叠组件下方)
```

```
FileExplorer Structure:
             └── 主布局（QVBoxLayout）
                   ├── 标题栏（QLabel，"资源管理器"）
                   └── 水平分割器（QSplitter，左右分栏）
                         ├── 左侧文件树（QTreeWidget）
                         │     └── 根节点（input_dir 和 output_dir）
                         │           └── 子节点（递归显示文件/文件夹，含图标）
                         └── 右侧容器（QWidget，垂直布局）
                               ├── 预览工具栏（PreviewToolbar）
                               │     ├── 执行按钮（execute_btn）
                               │     ├── 刷新按钮（refresh_btn）
                               │     └── 显示按钮（display_btn）
                               └── 预览堆叠组件（QStackedWidget）
                                     ├── 文本预览视图（QTextEdit，index 0）
                                     └── 图片预览视图（QLabel，index 1）
```

```
ListenerPage Structure:
             └── 主布局（QVBoxLayout）
                   ├── 标题栏（QLabel，"屏幕监听器"）
                   └── 右侧容器（QWidget，垂直布局）
                         ├── 监听器工具栏（ListenerToolbar）
                         │     ├── 执行按钮（execute_btn，"开始监听"）
                         │     └── 显示输出按钮（display_btn，"显示输出"）
                         └── 监听器参数设置组件（ListenerSettingsWidget）
                               └── 主水平布局（QHBoxLayout）
                                     ├── 设置框（QFrame）
                                     │     └── 垂直布局（QVBoxLayout）
                                     │           ├── 标题（QLabel，"监听器参数设置"）
                                     │           ├── 操作类型选择（QHBoxLayout）
                                     │           │     ├── 标签（QLabel，"操作类型:"）
                                     │           │     └── 下拉框（QComboBox，含ACTION_CHOICE选项）
                                     │           ├── 输入文件设置（QHBoxLayout）
                                     │           │     ├── 标签（QLabel，"输入文件:"）
                                     │           │     ├── 输入框（QLineEdit）
                                     │           │     └── 浏览按钮（QPushButton，"浏览..."）
                                     │           ├── 输出文件设置（QHBoxLayout）
                                     │           │     ├── 标签（QLabel，"输出文件:"）
                                     │           │     ├── 输入框（QLineEdit）
                                     │           │     ├── 浏览按钮（QPushButton，"浏览..."）
                                     │           │     ├── 输入框（QLineEdit）
                                     │           │     └── 输入框（QLineEdit）
                                     │           └── 弹性空间（Stretch）
                                     └── 帮助信息框（QFrame）
                                           └── 垂直布局（QVBoxLayout）
                                                 ├── 帮助标题（QLabel，"操作说明"）
                                                 └── 帮助内容（QTextEdit，含各类操作说明文本）
```

```
PaintingsPage Structure:
             └── 主布局（QVBoxLayout）
                   ├── 标题栏（QLabel，"画作列表"）
                   └── 主体水平布局（QHBoxLayout）
                         ├── 左侧名称列表（NavigationBar）
                         │     └── 项目列表（加载input和output的共有文件夹名）
                         └── 右侧水平分割器（QSplitter）
                               ├── 命令文本预览区（QTextEdit）
                               │     └── 只读文本显示（默认显示占位提示）
                               └── 图片展示区（QLabel）
                                     └── 居中对齐的图片/提示文本（默认显示选择提示）
```

```
AIPage Structure:
             └── 主布局（QVBoxLayout）
                   ├── 标题栏（QLabel，"AI作画"）
                   │     └── 固定高度（TITLE_HEIGHT常量）
                   ├── 历史对话记录显示区（QTextEdit）
                   │     ├── 只读模式（setReadOnly(True)）
                   │     └── 占位文本（"历史对话记录将在此显示..."）
                   └── 输入与发送区域（QHBoxLayout）
                         ├── 输入框（QTextEdit）
                         │     ├── 固定高度（120px）
                         │     └── 占位文本（"请输入提示词..."）
                         └── 发送按钮（QPushButton，"发送"）
                               ├── 固定高度（120px）
                               └── 点击触发on_send_clicked事件
```

```
SettingsPage Structure:
             └── 主布局（QHBoxLayout）
                   ├── 左侧设置导航栏（NavigationBar）
                   │     └── 项目列表（加载SETTING_TYPES定义的设置类型）
                   │           ├── 自动操作速度设置（默认选中项）
                   │           └── 监听器设置
                   └── 右侧设置堆叠组件（QStackedWidget）
                         ├── 自动操作速度设置页面（AutoOperationSpeedPage，index 0）
                         │     ├── 表单布局（QFormLayout）
                         │     │     ├── 倍速因子设置（QDoubleSpinBox，范围0.1-5.0）
                         │     │     ├── 基础绘图时间1（QDoubleSpinBox，范围0.01-2.0）
                         │     │     ├── 基础绘图时间2（QDoubleSpinBox，范围0.01-2.0）
                         │     │     ├── 基础绘图时间3（QDoubleSpinBox，范围0.01-2.0）
                         │     │     ├── 点击等待时间（QDoubleSpinBox，范围0.01-2.0）
                         │     │     ├── 鼠标移动时间（QDoubleSpinBox，范围0.01-2.0）
                         │     │     └── 额外移动延迟（QDoubleSpinBox，范围0.01-1.0）
                         │     └── 确定按钮（QPushButton，底部固定高度40px）
                         └── 监听器设置页面（ListenerSettingPage，index 1）
                               └── 垂直布局（QVBoxLayout）
                                     ├── 命令打印开关（QCheckBox，"启用命令打印 (print_commands)"）
                                     └── 伸缩项（Stretch，使内容靠上显示）
```