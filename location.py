from pynput import keyboard
import pyautogui
import os

# 存储获取的位置
coords = []
# 位置文件
positions_file = "positions.txt"

def save_positions_to_file():
    with open(positions_file, "w") as file:
        for i, (x, y) in enumerate(coords, start=1):
            file.write(f"Position {i}: ({x}, {y})\n")
    print(f"Positions saved to {positions_file}")

def on_press(key):
    try:
        if key == keyboard.Key.space:
            # 获取鼠标当前位置
            x, y = pyautogui.position()
            coords.append((x, y))
            print(f"Captured position {len(coords)}: ({x}, {y})")
            
            # 检查是否已经获取了三个位置
            if len(coords) == 3:
                save_positions_to_file()
                return False  # 停止监听器
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    pass

# 启动监听器
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
