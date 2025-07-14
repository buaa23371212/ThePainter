import time
from pynput import mouse
from threading import Thread

# 存储点击事件的列表
clicks = []

def on_click(x, y, button, pressed):
    """鼠标点击回调函数"""
    if pressed:  # 只记录按下事件（忽略释放事件）
        timestamp = time.time() - start_time
        clicks.append({
            'time': f"{timestamp:.3f}s",
            'position': (x, y),
            'button': str(button).split('.')[-1]
        })

def record_clicks():
    """记录鼠标点击10秒钟"""
    global start_time
    start_time = time.time()
    
    print("开始记录鼠标点击（10秒）...")
    # 创建鼠标监听器
    with mouse.Listener(on_click=on_click) as listener:
        time.sleep(10)
        listener.stop()
    
    # 打印结果
    print("\n记录结果：")
    print(f"{'时间':<8} | {'坐标':<15} | {'按键'}")
    print("-" * 35)
    for click in clicks:
        print(f"{click['time']:<8} | {str(click['position']):<15} | {click['button']}")
    
    print(f"\n共检测到 {len(clicks)} 次点击")

if __name__ == "__main__":
    record_clicks()