# Thonny

## 安装 Thonny和在Pico上配置python环境

Thonny下下载软件 : https://thonny.org/

## Raspberry Pi Pico 配置python环境

要在Raspberry Pi Pico上安装MicroPython UF2文件，可以按照以下步骤操作：

#### 1. 下载MicroPython UF2文件

1. 打开你的浏览器并访问[Raspberry Pi Pico的MicroPython下载页面](https://micropython.org/download/rp2-pico/)。

2. 找到最新版本的MicroPython UF2文件，并点击下载。

#### 2. 将Raspberry Pi Pico连接到计算机

1. 按住Raspberry Pi Pico上的BOOTSEL按钮。

2. 按住BOOTSEL按钮的同时，将Pico通过USB线连接到计算机。

3. 松开BOOTSEL按钮。此时，Pico应该会以USB存储设备的形式出现在你的计算机上，通常名为 "RPI-RP2"。

#### 3. 拷贝MicroPython UF2文件到Pico

1. 打开你的计算机上的文件管理器。

2. 找到刚才下载的MicroPython UF2文件。

3. 将MicroPython UF2文件拖到RPI-RP2驱动器中。

4. 文件复制完成后，Pico将自动重启并运行MicroPython。RPI-RP2驱动器会从文件管理器中消失。

#### 4. 在Thonny中设置Pico

1. 打开Thonny。

2. 在Thonny中，点击“工具”（Tools）菜单，然后选择“选项”（Options）。

3. 在选项对话框中，选择“解释器”（Interpreter）选项卡。

4. 在“解释器”下拉菜单中，选择“MicroPython (Raspberry Pi Pico)”。

5. 在“端口”下拉菜单中，选择你Pico连接的端口。通常，Thonny会自动检测到正确的端口。

6. 点击“确定”以保存设置。

#### 5. 测试MicroPython

1. 在Thonny中打开一个新的文件。

2. 输入以下简单的Python代码来测试Pico是否工作正常：
   ```python
   print("Hello, Raspberry Pi Pico!")
   ```

3. 点击运行按钮（绿色的运行箭头），然后选择“保存并运行”。

4. 如果Pico正常工作，你应该会在Thonny的Shell窗口中看到输出“Hello, Raspberry Pi Pico!”。

通过这些步骤，你就可以在Raspberry Pi Pico上成功安装MicroPython UF2文件，并在Thonny中进行编程了。如果遇到任何问题，请随时告诉我！

#### 6. python 依赖安装

<img src="images//image-20240728153333911.png" alt="image-20240728153333911" style="zoom:50%;" />

<img src="images//image-20240728153458503.png" alt="image-20240728153458503" style="zoom:50%;" />