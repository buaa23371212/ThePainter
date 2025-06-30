
[Toc]

# 指令集说明

---

## 圆形示例

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

## 椭圆示例

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

## 矩形示例

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

## 正方形示例

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

## 圆角矩形示例

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

## 线段示例

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

## 多边形示例

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

## 批量执行

- 执行文件中的多个命令  
  格式: `-input_file <path>`
  ```shell
  python main.py -input_file input/Sample-1/commands.txt