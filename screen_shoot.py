import pyautogui
from pynput import keyboard
import time
import os

screenshot_dir = "/Users/lintianjian/Downloads/药化/十七" 
with open("positions.txt", "r") as file:
    positions = file.readlines()
    x1, y1 = map(int, positions[0].split(":")[1].strip()[1:-1].split(","))
    x2, y2 = map(int, positions[1].split(":")[1].strip()[1:-1].split(","))
    x3, y3 = map(int, positions[2].split(":")[1].strip()[1:-1].split(","))
    region = (x1, y1, x3 - x1, y2 - y1)
#     file.close()
# region = (203, 50, 1920, 1080)

def on_press(key):
    try:
        # 检查是否按下了 down 键
        if key == keyboard.Key.cmd:
            # 使用当前时间生成唯一的文件名
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)
            
            # 截图并保存
            screenshot = pyautogui.screenshot(region=region)
            screenshot.save(filepath)
            print(f"Screenshot taken and saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    print(f'Key {key} released')
    if key == keyboard.Key.esc:
        # 停止监听
        return False



# 启动监听器
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()