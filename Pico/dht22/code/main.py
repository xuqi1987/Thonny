from machine import Pin, I2C
import ssd1306
import dht
import time

# 定义引脚
DHTPIN = 16  # DHT22 数据引脚连接到 GP16
OLED_SCL = 5  # I2C 时钟引脚
OLED_SDA = 4  # I2C 数据引脚

# 初始化 DHT 传感器
dht_sensor = dht.DHT22(Pin(DHTPIN))

# 初始化 I2C 接口和 OLED 显示屏
i2c = I2C(0, scl=Pin(OLED_SCL), sda=Pin(OLED_SDA))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

previous_time = time.ticks_ms()
interval = 3000  # 3秒间隔
show_temperature = True  # 切换显示标志


# 自定义字体数据（16x16字体）
font = {
    '0': [0x3E, 0x51, 0x49, 0x45, 0x3E],
    '1': [0x00, 0x42, 0x7F, 0x40, 0x00],
    '2': [0x72, 0x49, 0x49, 0x49, 0x46],
    '3': [0x21, 0x41, 0x49, 0x4D, 0x33],
    '4': [0x18, 0x14, 0x12, 0x7F, 0x10],
    '5': [0x27, 0x45, 0x45, 0x45, 0x39],
    '6': [0x3C, 0x4A, 0x49, 0x49, 0x30],
    '7': [0x01, 0x71, 0x09, 0x05, 0x03],
    '8': [0x36, 0x49, 0x49, 0x49, 0x36],
    '9': [0x06, 0x49, 0x49, 0x29, 0x1E],
    '.': [0x00, 0x00, 0x60, 0x60, 0x00],
    '%': [0x62, 0x64, 0x08, 0x13, 0x23],
    'C': [0x3E, 0x41, 0x41, 0x41, 0x22],
    '温': [0x24, 0xA4, 0xA4, 0xFF, 0xA4, 0xA4, 0x24],
    '度': [0xFF, 0x24, 0x24, 0xA4, 0xA4, 0xA4, 0x64],
    '湿': [0xFF, 0x10, 0x28, 0xC6, 0x10, 0x10, 0x10],
    '度': [0xFF, 0x24, 0x24, 0xA4, 0xA4, 0xA4, 0x64],
}

def draw_char(oled, char, x, y, size=1):
    if char not in font:
        return
    data = font[char]
    for i in range(len(data)):
        for j in range(16):
            if data[i] & (1 << j):
                for a in range(size):
                    for b in range(size):
                        oled.pixel(x + i * size + a, y + j * size + b, 1)

def display_text(oled, text, x=10, y=10, size=1):
    oled.fill(0)
    offset = 0
    for char in text:
        draw_char(oled, char, x + offset, y, size)
        offset += 8 * size
    oled.show()



def read_dht_sensor():
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        return temperature, humidity
    except OSError as e:
        print("Failed to read from DHT sensor.")
        return None, None

def main():
    global previous_time, show_temperature
    while True:
        current_time = time.ticks_ms()

        if time.ticks_diff(current_time, previous_time) >= interval:
            previous_time = current_time
            show_temperature = not show_temperature  # 切换显示内容

        temperature, humidity = read_dht_sensor()

        if temperature is None or humidity is None:
            print("Failed to read from DHT sensor!")
            display_text(oled, "...", size=2)
        else:
            if show_temperature:
                display_text(oled, "{:.1f}C".format(temperature), size=3)
            else:
                display_text(oled, "{:.1f}%".format(humidity), size=3)

        time.sleep(1)  # 小延迟以防止高频率刷新

if __name__ == "__main__":
    main()