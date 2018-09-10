# 下拉框.py
import tkinter
from tkinter import ttk

root = tkinter.Tk()
xiala = tkinter.StringVar()
xialaselect = ttk.Combobox(root, width=12, 
                            textvariable=xiala)
xialaselect['values'] = ('老师', '学生')
xialaselect.pack()
xialaselect.current(0)
root.mainloop()