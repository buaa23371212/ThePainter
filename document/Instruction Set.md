
[Toc]

# 指令集说明

---

## 图形绘制命令

### 圆形

- 通过边界框绘制圆形  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python painter.py circle -bounding 500 300 700 500
  ```

- 通过圆心和半径绘制圆形  
  格式: `-center <center_x> <center_y> <radius>`
  ```shell
  python painter.py circle -center 600 400 200
  ```

---

### 椭圆

- 通过边界框绘制椭圆  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python painter.py ellipse -bounding 400 300 800 500
  ```

- 通过中心点和长短轴绘制椭圆  
  格式: `-center <center_x> <center_y> <semi_major_axis> <semi_minor_axis>`
  ```shell
  python painter.py ellipse -center 600 400 300 150
  ```

---

### 矩形

- 通过边界框绘制矩形  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python painter.py rectangle -bounding 500 300 700 500
  ```

- 通过中心点和尺寸绘制矩形  
  格式: `-center <center_x> <center_y> <width> <height>`
  ```shell
  python painter.py rectangle -center 600 400 200 200
  ```

---

### 正方形

- 通过边界框绘制正方形  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python painter.py square -bounding 400 400 600 600
  ```

- 通过中心点和边长绘制正方形  
  格式: `-center <center_x> <center_y> <size>`
  ```shell
  python painter.py square -center 500 500 200
  ```

---

### 圆角矩形

- 通过边界框绘制圆角矩形（包含圆角半径）  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python painter.py rounded_rectangle -bounding 500 300 700 500
  ```

- 通过中心点、尺寸和圆角半径绘制圆角矩形  
  格式: `-center <center_x> <center_y> <width> <height> <radius>`
  ```shell
  python painter.py rounded_rectangle -center 600 400 200 100 30
  ```

---

### 线段

- 通过起点和终点坐标绘制直线  
  格式: `-points <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python painter.py line -points 500 300 700 500
  ```

- 通过起点和方向向量绘制直线  
  格式: `-vector <start_x> <start_y> <dx> <dy>`
  ```shell
  python painter.py line -vector 500 300 200 200
  ```

---

### 曲线

- 通过控制点直接绘制贝塞尔曲线  
  格式: `-points <x0> <y0> <x1> <y1> <x2> <y2> <x3> <y3>`
  ```shell
  python painter.py curve -points 500 300 300 300 500 500 700 500
  ```
  上述命令将使用起点 (x0, y0)、终点 (x3, y3) 以及两个控制点 (x1, y1)、(x2, y2) 绘制一条三次贝塞尔曲线。

- 通过JSON文件和ID绘制曲线  
  格式: `-file <path> -id <curve_id>`
  ```shell
  python painter.py curve -file input/Sample-1/shapes.json -id curve1
  ```
  上述命令会从指定的JSON文件中查找ID为`curve1`的曲线，并按其控制点绘制。

- 通过JSON文件和名称绘制曲线  
  格式: `-file <path> -name "<curve_name>"`
  ```shell
  python painter.py curve -file input/Sample-1/shapes.json -name "mycurve"
  ```
  上述命令会从JSON文件中查找名称为`mycurve`的曲线并绘制。
  
---

### 多边形

- 直接指定顶点绘制多边形  
  格式: `-vertices <x1> <y1> <x2> <y2> ...`
  ```shell
  python painter.py polygon -vertices 500 300 700 500 300 500
  ```

- 通过JSON文件和名称绘制多边形  
  格式: `-file <path> -name "<polygon_name>"`
  ```shell
  python painter.py polygon -file input/Sample-1/shapes.json -name "filled triangle"
  ```

- 通过JSON文件和ID绘制多边形  
  格式: `-file <path> -id <polygon_id>`
  ```shell
  python painter.py polygon -file input/Sample-1/shapes.json -id star
  ```

---

## 鼠标控制命令

- 移动鼠标到指定位置  
  格式: `-x <X_COORD> -y <Y_COORD>`
  ```shell
  python painter.py move_mouse -x 800 -y 600
  ```

- 在指定位置模拟鼠标点击  
  格式: `-x <X_COORD> -y <Y_COORD>`
  ```shell
  python painter.py mouse_click -x 800 -y 600
  ```

- 在指定位置模拟鼠标右键点击  
  格式: `-x <X_COORD> -y <Y_COORD>`
  ```shell
  python painter.py right_click -x 800 -y 600
  ```

---

## 图层控制命令

- 添加新图层  
  格式: 无参数
  ```shell
  python painter.py add_layer
  ```

- 选择指定图层  
  格式: `-layer_id <图层ID>`
  ```shell
  python painter.py choose_layer -layer_id 2
  ```

- 对指定图层执行操作  
  格式: `-operation <操作类型> -layer_id <图层ID>`
  - 操作类型可选：`hide`（隐藏/显示）、`copy`（复制）、`merge_down`（向下合并）、`move_up`（上移）、`move_down`（下移）、`delete`（删除）
  - 图层ID默认为1（顶部图层）
  ```shell
  python painter.py layer_operation -operation hide -layer_id 1
  python painter.py layer_operation -operation copy -layer_id 2
  python painter.py layer_operation -operation delete -layer_id 3
  ```

---

## 填充工具命令

- 选择指定线条颜色

  你可以通过 `-color <颜色>` 参数指定线条颜色，有两种用法：

  1. **全局指定颜色（影响后续所有命令）**  
     单独执行 `python painter.py -color <颜色>`，会将当前线条颜色切换为指定颜色，影响后续所有未显式指定 `-color` 的命令。例如：

     ```shell
     python painter.py -color red
     python painter.py circle -bounding 500 300 700 500
     python painter.py rectangle -bounding 100 100 200 200
     ```
     上述命令后，圆和矩形都会用红色线条绘制，直到再次切换颜色。

  2. **临时指定颜色（只影响本条命令，并将全局颜色切换为该颜色）**  
     在具体绘图命令前加 `-color`，会切换当前颜色，并用该颜色绘制。例如：

     ```shell
     python painter.py -color black circle -bounding 500 300 700 500
     ```
     上述命令会绘制一个黑色边界的圆，且接下来所有的线条也都是黑色，直到再次切换颜色。

  - 支持的颜色有：

- 对指定位置进行颜色填充  
  格式: `fill -color <颜色> -x <X坐标> -y <Y坐标>`
  ```shell
  python painter.py fill -color red -x 500 -y 400
  ```
  该命令会在 (500, 400) 位置用红色进行填充, 并将全局颜色切换为该颜色。

---

## 文本工具命令

- 在指定位置新建文本框并输入文本
  格式: `text -text <文本> -x <X坐标> -y <Y坐标>`
  ```shell
  python painter.py fill text -text test -x 500 -y 500
  ```
  该命令会在 (500, 500) 位置新建文本框，并输入test
---

## 批量执行

- 执行文件中的多个命令  
  格式: `-input_file <path>`
  ```shell
  python painter.py -input_file input/Sample-1/commands.txt
  ```
---

## 批量执行命令文件格式

命令文件(.txt)应包含一系列绘图命令，每行一个命令，格式如下：

```
命令名称 [参数]...
```

### 示例命令文件 (command.txt)
```shell
# 激活画布窗口
mouse_click -x 1000 -y 50

# 设置黑色为默认线条颜色
-color black

# 绘制地基（横长方形）
rectangle -center 960 860 800 100

# 绘制主体（竖长方形）
rectangle -center 960 660 600 400

# 绘制门
rectangle -center 760 715 100 180

# 更多命令...
```

### 命令文件说明
1. 每行一个命令，以命令名称开头
2. 参数按顺序排列，使用空格分隔
3. 支持注释（以`#`开头的行）
4. 命令顺序执行，从上到下
5. 可引用外部JSON文件（如`-file shapes.json`）

---

## JSON 文件格式说明

程序支持通过 JSON 文件定义多边形、曲线和多段曲线路径。以下是完整的 JSON 格式规范：

### 多边形 (polygons)
```json
"polygons": {
  "<多边形ID>": {
    "vertices": [
      [x1, y1],
      [x2, y2],
      // 更多顶点...
    ],
    "closed": true/false  // 可选，是否闭合路径（默认 true）
  },
  // 更多多边形...
}
```

### 曲线 (curves - 单条贝塞尔曲线)
```json
"curves": {
  "<曲线ID>": {
    "name": "<曲线名称>",  // 可选
    "points": [
      [起点_x, 起点_y],
      [控制点1_x, 控制点1_y],
      [控制点2_x, 控制点2_y],
      [终点_x, 终点_y]
    ]
  },
  // 更多曲线...
}
```

### 多段曲线路径 (multicurves - 多条连续贝塞尔曲线)
```json
"multicurves": {
  "<路径ID>": {
    "name": "<路径名称>",  // 可选
    "points": [
      [起点_x, 起点_y],
      [控制点1_x, 控制点1_y],
      [控制点2_x, 控制点2_y],
      [终点/下一段起点_x, 终点/下一段起点_y],
      // 后续曲线段控制点（每段需要3个新点）...
    ]
  },
  // 更多路径...
}
```

### 完整 JSON 示例
```json
{
  "polygons": {
    "triangle": {
      "vertices": [[500, 300], [700, 500], [300, 500]]
    },
    "star": {
      "vertices": [[600,200],[700,350],[900,350],[750,450],[800,600],[600,500],[400,600],[450,450],[300,350],[500,350]]
    }
  },
  "curves": {
    "curve1": {
      "name": "Single Curve",
      "points": [[500,300], [300,300], [500,500], [700,500]]
    }
  },
  "multicurves": {
    "path1": {
      "name": "Complex Path",
      "points": [[500,300],[300,300],[500,500],[700,500],[600,400],[400,400],[600,600],[800,600]]
    }
  }
}
```

### 使用说明
1. 多边形顶点按顺序连接，最后顶点默认连接回第一个顶点
2. 单条曲线需要精确的 4 个点（起点 + 2控制点 + 终点）
3. 多段曲线路径的点数需为 `3n+1`（n=曲线段数）
4. 在命令中使用 `-id` 参数引用对象ID，或用 `-name` 引用对象名称
