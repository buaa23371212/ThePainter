- 默认行为（记录并打印鼠标事件）
  ```shell
  python listener_cli.py
  ```

- 记录并导出到文件
  默认路径
  ```shell
  python listener_cli.py -a export
  ```
  指定路径
  ```shell
  python listener_cli.py -a export -c path/to/output.json
  ```

- 记录并转换（不打印命令）
  ```shell
  python listener_cli.py -a convert
  ```

- 记录、转换并打印命令
  ```shell
  python listener_cli.py -a full
  ```

- 从文件解析并转换（不打印命令）
  ```shell
  python listener_cli.py -a parse -f path/to/file.json
  ```

- 从文件解析、转换并保存绘图命令
  ```shell
  python listener_cli.py -a parse_and_save -f path/to/input.json -c path/to/output.pcmd
  ```

- 从文件解析、转换并打印命令
  ```shell
  python listener_cli.py -a parse -f path/to/file.json -p
  ```