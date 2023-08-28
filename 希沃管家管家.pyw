import tkinter as tk
import configparser
import psutil
import subprocess
import tkinter.messagebox as messagebox
import os
import time
import json
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

    # 测试运行配置项
    test_run = tk.Label(config_window, text="测试运行时长:")
    test_run.pack()
    test_run_entry = tk.Entry(config_window, width=60, font=("Arial", 22))
    test_run_entry.insert(tk.END, config.get('Variables', 'test_run'))
    test_run_entry.pack()

    # 保存配置并关闭窗口的函数
    def save_and_close():
        config.set('Variables', 'program_name', program_name_entry.get())
        config.set('Variables', 'photo_name', photo_name_entry.get())
        config.set('Variables', 'x', x_entry.get())
        config.set('Variables', 'y', y_entry.get())
        config.set('Variables', 'delay', delay_entry.get())
        config.set('Variables', 'target_width', target_width_entry.get())
        config.set('Variables', 'target_height', target_height_entry.get())
        config.set('Variables','test_run',test_run_entry.get())

        with open('config.txt', 'w') as config_file:
            config.write(config_file)

        config_window.destroy()
    # 测试按钮配置项
    def save_and_execute():
        # 记录当前 program_name 的值并临时存储到 pro_name 变量中
        pro_name = config.get('Variables', 'program_name')
        run_time =int(config.get('Variables','test_run'))
        
        # 修改 program_name 的值为 cmd.exe
        config.set('Variables', 'program_name', 'cmd.exe')
        
        with open('config.txt', 'w') as config_file:
            config.write(config_file)
        
        # 打开 cmd.exe 并运行 seewocontrol.exe
        os.system('start cmd.exe /c "seewocontrol.exe"')
        
        # 等待 
        time.sleep(run_time)
        
        # 关闭 cmd.exe 和 seewocontrol.exe
        os.system('taskkill /f /im cmd.exe')
        os.system('taskkill /f /im seewocontrol.exe')
        
        # 将 pro_name 的值重新赋值给 config.txt 中的 program_name
        config.set('Variables', 'program_name', pro_name)
        
        with open('config.txt', 'w') as config_file:
            config.write(config_file)

    # 保存并退出按钮
    save_button = tk.Button(config_window, text="保存并退出", command=save_and_close, width=80, height=2)
    save_button.pack()
    
    # 保存并执行按钮
    save_button = tk.Button(config_window, text="测试运行（如果测试运行时长修改，请先保存）", command=save_and_execute, width=80, height=2)
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
