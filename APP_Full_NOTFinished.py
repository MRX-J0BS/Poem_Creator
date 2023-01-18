import tkinter as tk
import PCear_FullFunction
import os
import time
os.system('python3 --version')





def window2(): #把诗词复原窗口做成函数，这样就可以弹出独立窗口
    def reshow(key):
        output = PCear_FullFunction.remakealetter_random(key=key, num=5, time=4)
        text_output_remake.insert('insert', '________________复原了一首诗________________ \n')
        text_output_remake.insert('insert', output)
        text_output_remake.insert('insert', '_____________生成结束，感谢使用_____________ \n')

    remakeWindow = tk.Tk()
    remakeWindow.geometry('700x500')
    remakeWindow.title('诗词复原界面')

    label_whoami=tk.Label(remakeWindow,text='唯一作者MRX 禁止任何传播或商业行为 包括个人使用',bg='red')
    label_whoami.pack()
    #key_input = tk.StringVar()
    entry_key = tk.Entry(remakeWindow)
    entry_key.pack()
    key_input=entry_key.get()


    button_make = tk.Button(remakeWindow, text='复原一首诗', command=reshow(key=key_input))
    button_make.pack()

    text_output_remake = tk.Text(remakeWindow, width=90)
    text_output_remake.pack()

    tk.mainloop()


def window1():
    def show():
        output = PCear_FullFunction.makeALetter(num=5, time=4, mode='letter+key')
        text_output.insert('insert', '________________生成了一首诗________________ \n')
        text_output.insert('insert', output)
        text_output.insert('insert', '_____________生成结束，感谢使用_____________ \n')
        time.sleep(3)


    main = tk.Tk()
    main.geometry('750x500')
    main.title('诗意——失义')

    label_whoami=tk.Label(main,text='唯一作者MRX 禁止任何传播或商业行为 包括个人使用',bg='red')
    label_whoami.pack()

    button_make = tk.Button(main, text='生成一首诗', command=show)
    button_make.pack()

    button_remake = tk.Button(main, text='复原一首诗', command=window2)
    button_remake.pack()

    text_output = tk.Text(main, width=90)
    text_output.pack()
    tk.mainloop()

if __name__=='__main__':
    window1()

