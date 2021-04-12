'''
随机点名软件功能：

1. 打开表格（名称必须为“name.xls”，且与程序处于同一文件夹目录）添加姓名，每行一个
2. 点击“开始点名”对姓名随机抽取
3. 滚动显示姓名，就是对所有姓名快速显示
4. 对抽取的人名放大显示，系统播报该名字（继续点击“开始点名”）
5. 勾选“重复点名”按钮，则被点过的名字还有可能被点到
6. 出现错误时关闭弹框后继续使用

Copyright(C) 2020, Bob Frank
'''

import win32com.client as win
import pandas as pd
from tkinter import Label, Text, Button, Tk, StringVar, IntVar, Checkbutton, mainloop
import random
import time
from PIL import ImageTk, Image


def readText():
    data = pd.read_excel("./name.xls")  # 读入文件
    data = list(data['姓名'])
    return data


def nameRandom():
    global CheckVar1, name_data1, name_data2
    if CheckVar1.get() == 1:  # if clicked
        index = random.randint(0, len(name_data1) - 1)
        str = name_data1[index]
    else:
        if len(name_data2) == 0:
            newGui = Tk(className="错误")
            newGui.geometry("480x240+220+90")
            error = Label(newGui, font=('SimHei', 20), text='所有人都点过了\n请重启软件！', fg='red')
            error.pack()
            return '0'
        else:
            index = random.randint(0, len(name_data2) - 1)
            str = name_data2[index]
            name_data2.remove(str)
    return str


def readStr(str):
    speak = win.Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def run():
    # 设置全局变量
    global name_data1, name_data2, round_text, name_text, name, last_name, round_text
    # 刷新被点名人
    last_name.set('被点名：')
    name_text.update()

    str = nameRandom()
    print(name_data1)
    for i in range(0, 50):
        index = random.randint(0, len(name_data1) - 1)
        name.set('随机滚动：' + name_data1[index])
        round_text.update()
        time.sleep(0.08)
    last_name.set('被点名：' + str)
    name_text.update()
    # 刷新滚动名字
    name.set('随机滚动：')
    round_text.update()
    readStr(str)


# 开始
name_data1 = list(readText())
name_data2 = list(name_data1)
print(name_data1)

# 设置界面
gui = Tk(className="随机点名")

gui.geometry("720x520+220+90")
label = Label(gui, font=('SimHei', 30), text='随机点名软件')
label.pack()

# 导引
text = Text(gui, height=11, font=('SimHei', 11), fg='#636363')
text.insert(1.0, '随机点名软件功能：\n\n'
                 '1. 表格名称必须为“name.xls”,且与程序处于同一文件夹目录,添加姓名,每行一个\n'
                 '2. 点击“开始点名”对姓名随机抽取\n'
                 '3. 滚动显示姓名，对所有姓名快速显示\n'
                 '4. 对抽取的姓名特殊显示，系统播报该名字(继续点击“开始点名”可再次点名)\n'
                 '5. 勾选“重复点名”按钮，则被点过的名字还可能被点到\n'
                 '6. 出现错误时关闭弹框后重启程序\n\n'
                 'Copyright(C) 2020, Bob Frank\n')
text.pack()

# 动态文本
name = StringVar()
name.set('随机滚动：')
last_name = StringVar()
last_name.set('被点名：')

# 滚动文本
round_text = Label(gui, height=1, textvariable=name, font=('SimHei', 15), fg='#000000')
round_text.pack()

# 最终显示文本
name_text = Label(gui, height=1, textvariable=last_name, font=('SimHei', 15), fg='#FF7F00')
name_text.pack()

# 按钮
btn1 = Button(gui, text='开始点名', bg='#32CD32', fg='#ffffff', font=('SimHei', 15),
              command=run)
btn1.pack()

# 复选框
CheckVar1 = IntVar()
label_again = Checkbutton(gui, text='重复点名', onvalue=1, offvalue=0, variable=CheckVar1, font=('SimHei', 15))
label_again.pack()

# 背景图
bgImage = ImageTk.PhotoImage((Image.open('./background.jpg')).resize((240, 180)))
img = Label(gui, image=bgImage)
img.pack()

mainloop()

