# -_ktp

## 半手动的截图工具

可以让你在按下特定键时对屏幕的特定区域进行截图

特别是针对某些莫名其妙设置了下载权限的网站

自己看一遍的同时也截下了所有的图

## 操作方式

先下载库

```zsh
pip install pyautogui pynput
```

再运行`location.py`定位, 默认先左上, 后左下, 右上

每次按下空格即可

然后可以在`screen_shoot.py`里改键位`<key>`

```python
if key == keyboard.Key.<key>:
```
