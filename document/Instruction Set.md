
[Toc]

# 指令集说明

---

## 图形绘制命令

### 圆形

- 通过边界框绘制圆形  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python main.py circle -bounding 500 300 700 500
  ```

- 通过圆心和半径绘制圆形  
  格式: `-center <center_x> <center_y> <radius>`
  ```shell
  python main.py circle -center 600 400 200
  ```

---

### 椭圆

- 通过边界框绘制椭圆  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python main.py ellipse -bounding 400 300 800 500
  ```

- 通过中心点和长短轴绘制椭圆  
  格式: `-center <center_x> <center_y> <semi_major_axis> <semi_minor_axis>`
  ```shell
  python main.py ellipse -center 600 400 300 150
  ```

---

### 矩形

- 通过边界框绘制矩形  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python main.py rectangle -bounding 500 300 700 500
  ```

- 通过中心点和尺寸绘制矩形  
  格式: `-center <center_x> <center_y> <width> <height>`
  ```shell
  python main.py rectangle -center 600 400 200 200
  ```

---

### 正方形

- 通过边界框绘制正方形  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python main.py square -bounding 400 400 600 600
  ```

- 通过中心点和边长绘制正方形  
  格式: `-center <center_x> <center_y> <size>`
  ```shell
  python main.py square -center 500 500 200
  ```

---

### 圆角矩形

- 通过边界框绘制圆角矩形（包含圆角半径）  
  格式: `-bounding <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python main.py rounded_rectangle -bounding 500 300 700 500
  ```

- 通过中心点、尺寸和圆角半径绘制圆角矩形  
  格式: `-center <center_x> <center_y> <width> <height> <radius>`
  ```shell
  python main.py rounded_rectangle -center 600 400 200 100 30
  ```

---

### 线段

- 通过起点和终点坐标绘制直线  
  格式: `-points <start_x> <start_y> <end_x> <end_y>`
  ```shell
  python main.py line -points 500 300 700 500
  ```

- 通过起点和方向向量绘制直线  
  格式: `-vector <start_x> <start_y> <dx> <dy>`
  ```shell
  python main.py line -vector 500 300 200 200
  ```

---

### 曲线

- 通过控制点直接绘制贝塞尔曲线  
  格式: `-points <x0> <y0> <x1> <y1> <x2> <y2> <x3> <y3>`
  ```shell
  python main.py curve -points 500 300 300 300 500 500 700 500
  ```
  上述命令将使用起点 (x0, y0)、终点 (x3, y3) 以及两个控制点 (x1, y1)、(x2, y2) 绘制一条三次贝塞尔曲线。

- 通过JSON文件和ID绘制曲线  
  格式: `-file <path> -id <curve_id>`
  ```shell
  python main.py curve -file input/Sample-1/shapes.json -id curve1
  ```
  上述命令会从指定的JSON文件中查找ID为`curve1`的曲线，并按其控制点绘制。

- 通过JSON文件和名称绘制曲线  
  格式: `-file <path> -name "<curve_name>"`
  ```shell
  python main.py curve -file input/Sample-1/shapes.json -name "mycurve"
  ```
  上述命令会从JSON文件中查找名称为`mycurve`的曲线并绘制。
  
---

### 多边形

- 直接指定顶点绘制多边形  
  格式: `-vertices <x1> <y1> <x2> <y2> ...`
  ```shell
  python main.py polygon -vertices 500 300 700 500 300 500
  ```

- 通过JSON文件和名称绘制多边形  
  格式: `-file <path> -name "<polygon_name>"`
  ```shell
  python main.py polygon -file input/Sample-1/shapes.json -name "filled triangle"
  ```

- 通过JSON文件和ID绘制多边形  
  格式: `-file <path> -id <polygon_id>`
  ```shell
  python main.py polygon -file input/Sample-1/shapes.json -id star
  ```

---

## 鼠标控制命令

- 移动鼠标到指定位置  
  格式: `-x <X_COORD> -y <Y_COORD>`
  ```shell
  python main.py move_mouse -x 800 -y 600
  ```

- 在指定位置模拟鼠标点击  
  格式: `-x <X_COORD> -y <Y_COORD>`
  ```shell
  python main.py mouse_click -x 800 -y 600
  ```

- 在指定位置模拟鼠标右键点击  
  格式: `-x <X_COORD> -y <Y_COORD>`
  ```shell
  python main.py right_click -x 800 -y 600
  ```

---

## 图层控制命令

- 添加新图层  
  格式: 无参数
  ```shell
  python main.py add_layer
  ```

- 选择指定图层  
  格式: `-layer_id <图层ID>`
  ```shell
  python main.py choose_layer -layer_id 2
  ```

- 对指定图层执行操作  
  格式: `-operation <操作类型> -layer_id <图层ID>`
  - 操作类型可选：`hide`（隐藏/显示）、`copy`（复制）、`merge_down`（向下合并）、`move_up`（上移）、`move_down`（下移）、`delete`（删除）
  - 图层ID默认为1（顶部图层）
  ```shell
  python main.py layer_operation -operation hide -layer_id 1
  python main.py layer_operation -operation copy -layer_id 2
  python main.py layer_operation -operation delete -layer_id 3
  ```

---

## 填充工具命令

- 选择指定线条颜色

  你可以通过 `-color <颜色>` 参数指定线条颜色，有两种用法：

  1. **全局指定颜色（影响后续所有命令）**  
     单独执行 `python main.py -color <颜色>`，会将当前线条颜色切换为指定颜色，影响后续所有未显式指定 `-color` 的命令。例如：

     ```shell
     python main.py -color red
     python main.py circle -bounding 500 300 700 500
     python main.py rectangle -bounding 100 100 200 200
     ```
     上述命令后，圆和矩形都会用红色线条绘制，直到再次切换颜色。

  2. **临时指定颜色（只影响本条命令，并将全局颜色切换为该颜色）**  
     在具体绘图命令前加 `-color`，会切换当前颜色，并用该颜色绘制。例如：

     ```shell
     python main.py -color black circle -bounding 500 300 700 500
     ```
     上述命令会绘制一个黑色边界的圆，且接下来所有的线条也都是黑色，直到再次切换颜色。

  - 支持的颜色有：`black`, `white`, `red`, `green`, `blue`, `yellow`, `gray`, `lightgray`, `darkgray`, `orange`, `purple`, `brown`

- 对指定位置进行颜色填充  
  格式: `fill -color <颜色> -x <X坐标> -y <Y坐标>`
  ```shell
  python main.py fill -color red -x 500 -y 400
  ```
  该命令会在 (500, 400) 位置用红色进行填充, 并将全局颜色切换为该颜色。

---

## 批量执行

- 执行文件中的多个命令  
  格式: `-input_file <path>`
  ```shell
  python main.py -input_file input/Sample-3/commands.txt