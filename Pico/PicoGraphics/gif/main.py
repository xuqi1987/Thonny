from pimoroni_bus import SPIBus
import time
from picographics import PicoGraphics, DISPLAY_LCD_240X240, PEN_RGB332
import pngdec
import os

# 初始化SPI总线和显示屏
spibus = SPIBus(cs=13, dc=8, sck=10, mosi=11)
display = PicoGraphics(display=DISPLAY_LCD_240X240, bus=spibus, pen_type=PEN_RGB332)

# 设置背光亮度
display.set_backlight(1.0)

# 创建PNG解码器实例
png = pngdec.PNG(display)

# 获取PNG图像文件列表
image_dir = "out"  # 确保这个目录路径是正确的
images = [ f"{image_dir}/{f}" for f in os.listdir(image_dir) if f.endswith('.png')]
images.sort()  # 确保按顺序加载

# 设置背景颜色和文本颜色
BG = display.create_pen(200, 200, 200)
TEXT = display.create_pen(0, 0, 0)

# 清屏并显示初始文本
display.set_pen(BG)
display.clear()
display.set_pen(TEXT)
display.text("PNG Animation", 15, 80)
display.update()

# 显示PNG图像的主循环
while True:
    start_time = time.time()
    for img_path in images:
        try:
            # 打开PNG文件并解码
            png.open_file(img_path)
            display.set_pen(BG)
            display.clear()
            png.decode(0, 0)  # 解码PNG文件并显示在屏幕上
        except OSError:
            print(f"Error: PNG File {img_path} missing.")
            continue
        
        display.update()
        
        # 控制帧率，使每秒钟显示10张图片
        #time.sleep(max(0, 0.1 - (time.time() - start_time)))
        time.sleep(1)
        start_time = time.time()