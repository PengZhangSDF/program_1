import tkinter as tk
import configparser
import psutil
import subprocess
import tkinter.messagebox as messagebox

def open_seewo():
    subprocess.Popen("seewocontrol.exe")

def close_seewo():
    closed = False  # 标记是否成功关闭希沃管家
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == "seewocontrol.exe":
            proc.kill()
            closed = True
    if closed:
        messagebox.showinfo("提示", "希沃管家管家已经关闭")
    else:
        messagebox.showinfo("提示", "希沃管家管家尚未启动")

def open_config_menu():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.txt')

    # 创建配置窗口
    config_window = tk.Toplevel()
    config_window.geometry("900x600")

    # 检测程序进程配置项
    program_name_label = tk.Label(config_window, text="检测程序进程:")
    program_name_label.pack()
    program_name_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    program_name_entry.insert(tk.END, config.get('Variables', 'program_name'))
    program_name_entry.pack()

    # 显示图片名称配置项
    photo_name_label = tk.Label(config_window, text="显示图片名称:")
    photo_name_label.pack()
    photo_name_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    photo_name_entry.insert(tk.END, config.get('Variables', 'photo_name'))
    photo_name_entry.pack()

    # x坐标配置项
    x_label = tk.Label(config_window, text="x坐标（从屏幕左上角向右，可以为负）:")
    x_label.pack()
    x_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    x_entry.insert(tk.END, config.get('Variables', 'x'))
    x_entry.pack()

    # y坐标配置项
    y_label = tk.Label(config_window, text="y坐标（从屏幕左上角向下，可以为负）:")
    y_label.pack()
    y_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    y_entry.insert(tk.END, config.get('Variables', 'y'))
    y_entry.pack()

    # 循环周期配置项
    delay_label = tk.Label(config_window, text="循环周期:")
    delay_label.pack()
    delay_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    delay_entry.insert(tk.END, config.get('Variables', 'delay'))
    delay_entry.pack()

    # 显示图片的长度配置项
    target_width_label = tk.Label(config_window, text="显示图片的长度:")
    target_width_label.pack()
    target_width_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    target_width_entry.insert(tk.END, config.get('Variables', 'target_width'))
    target_width_entry.pack()

    # 显示图片的宽度配置项
    target_height_label = tk.Label(config_window, text="显示图片的宽度:")
    target_height_label.pack()
    target_height_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    target_height_entry.insert(tk.END, config.get('Variables', 'target_height'))
    target_height_entry.pack()

    # 保存配置并关闭窗口的函数
    def save_and_close():
        config.set('Variables', 'program_name', program_name_entry.get())
        config.set('Variables', 'photo_name', photo_name_entry.get())
        config.set('Variables', 'x', x_entry.get())
        config.set('Variables', 'y', y_entry.get())
        config.set('Variables', 'delay', delay_entry.get())
        config.set('Variables', 'target_width', target_width_entry.get())
        config.set('Variables', 'target_height', target_height_entry.get())

        with open('config.txt', 'w') as config_file:
            config.write(config_file)

        config_window.destroy()

    # 保存并退出按钮
    save_button = tk.Button(config_window, text="保存并退出", command=save_and_close, width=10, height=2)
    save_button.pack()

root = tk.Tk()
root.geometry("900x600")

# 打开希沃管家按钮
open_seewo_button = tk.Button(root, text="打开希沃管家管家", command=open_seewo, width=80, height=10)
open_seewo_button.pack()

# 关闭希沃管家按钮
close_seewo_button = tk.Button(root, text="关闭希沃管家管家", command=close_seewo, width=80, height=10)
close_seewo_button.pack()


# 配置菜单按钮
config_menu_button = tk.Button(root, text="配置菜单", command=open_config_menu, width=80, height=5, bg="blue")
config_menu_button.pack()

root.mainloop()
