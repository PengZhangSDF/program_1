import cv2
import win32gui
import win32con
import time
import pygetwindow as gw
import psutil
import configparser

# 创建配置解析器对象
config = configparser.ConfigParser()
# 读取配置文件
config.read('config.txt')

# 从配置文件中获取变量的值
program_name = config.get('Variables', 'program_name')
photo_name = config.get('Variables', 'photo_name')
x = int(config.get('Variables', 'x'))
y = int(config.get('Variables', 'y'))
delay = float(config.get('Variables', 'delay'))
target_width = int(config.get('Variables', 'target_width'))
target_height = int(config.get('Variables', 'target_height'))

def check_program_status():
    camera_open = False
    cmd_open = False

    while True:
        current_cmd_open = False
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == program_name:
                current_cmd_open = True
                break

        if current_cmd_open:
            img = cv2.imread(photo_name)

            # 设置目标窗口尺寸
            # target_width = 15
            # target_height = 15

            # 显示图像
            cv2.imshow('jc', img)

            # 获取或创建名为 'jc' 的窗口
            jc_window = gw.getWindowsWithTitle('jc')[0]

            # 设置窗口的大小和位置
            jc_window.resizeTo(target_width, target_height)
            jc_window.moveTo(x, y)  # 将窗口移动到指定位置

            # 去掉窗口的边框和标题栏
            hwnd = win32gui.FindWindow(None, 'jc')
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            style = style & ~win32con.WS_CAPTION & ~win32con.WS_THICKFRAME
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

            # 设置窗口置顶
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)
        else:
            if cv2.getWindowProperty('jc', cv2.WND_PROP_VISIBLE) > 0:
                cv2.destroyWindow('jc')

        cv2.waitKey(1)

        time.sleep(delay)  # 延迟指定时间

    cv2.destroyAllWindows()


if __name__ == "__main__":
    check_program_status()
