import time
from machine import Pin, SPI
import st7789

# 定义引脚
TFT_CS = 13   # 片选引脚 GP10 (Pin 14)
TFT_RST = 9   # 复位引脚 GP9 (Pin 12)
TFT_DC = 8    # 数据/命令引脚 GP8 (Pin 11)
TFT_SDA = 11  # MOSI 引脚 GP11 (Pin 15)
TFT_SCL = 10  # SCK 引脚 GP13 (Pin 17)

# 初始化 SPI1 接口
spi = SPI(1, baudrate=40000000, polarity=1, phase=0, sck=Pin(TFT_SCL), mosi=Pin(TFT_SDA))

# 初始化其他引脚
cs = Pin(TFT_CS, Pin.OUT)
dc = Pin(TFT_DC, Pin.OUT)
rst = Pin(TFT_RST, Pin.OUT)

# 创建显示屏对象
tft = st7789.ST7789(spi, 240, 240, reset=rst, dc=dc, cs=cs)

# 初始化显示屏
tft.init()
tft.fill(st7789.BLACK)

# 绘制一个矩形
tft.fill_rect(0, 0, 240, 240, st7789.RED)

# 主循环
while True:
    # 每秒刷新一次，绘制不同颜色的矩形
    for color in [st7789.RED, st7789.GREEN, st7789.BLUE, st7789.YELLOW, st7789.WHITE]:
        tft.fill(st7789.BLACK)
        tft.fill_rect(0, 0, 240, 240, color)
        time.sleep(1)
