from src.main.python.terminal_logger.logger import info, error

def save_png(args):
    """
    保存当前画布为PNG文件

    步骤:
    1. 确保画图工具窗口是激活状态
    2. 发送Ctrl+S快捷键打开保存对话框
    3. 在文件名输入框中输入指定文件名
    4. 按Enter键确认保存

    注意:
    - 文件名输入框会自动聚焦，只需输入基本文件名
    - 系统会自动添加.png后缀
    - 如果文件已存在，系统会自动覆盖

    :param args: 包含保存参数的对象，需有file_name属性
    """
    try:
        # TODO: 手动最大化画图工具

        # 确保画布窗口激活
        # pyautogui.moveTo(CANVAS_BLANK_POSITION[0], CANVAS_BLANK_POSITION[1],
        #                  auto_speed_config.ACTUAL_MOUSE_MOVE_SPEED)
        # pyautogui.click()
        # time.sleep(auto_speed_config.ACTUAL_CLICK_WAIT)

        # # 发送保存快捷键 (Ctrl+S)
        # pyautogui.hotkey('ctrl', 's')
        # time.sleep(1.0)  # 等待保存对话框出现

        # # 输入文件名（系统会自动添加.png后缀）
        info(True, f"保存文件为: {args.file_name}.png", True)
        # pyautogui.write(args.file_name)
        # time.sleep(0.2)

        # # 按Enter键确认保存
        # pyautogui.press('enter')
        # time.sleep(0.5)  # 等待保存完成

    except Exception as e:
        error(True, f"保存文件失败: {str(e)}", True)