import tkinter as tk
import PCear_MainFunction

def show():
    output = PCear_MainFunction.makeALetter()
    text_output.insert('insert', '________________生成了一首诗________________ \n')
    text_output.insert('insert', output)
    text_output.insert('insert', '_____________生成结束，感谢使用_____________ \n')

main = tk.Tk()
main.geometry('750x500')
main.title('诗意——失义')

label_whoami=tk.Label(main,text='唯一作者MRX 禁止任何传播或商业行为 包括个人使用',bg='red')
label_whoami.pack()

button_make = tk.Button(main, text='生成一首诗', command=show)
button_make.pack()

text_output = tk.Text(main, width=90)
text_output.pack()

tk.mainloop()