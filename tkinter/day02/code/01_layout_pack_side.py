# layout_pack_side.py

import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, text="Label 1")
label2 = tkinter.Label(root, text='Label 2')
label3 = tkinter.Label(root, text='Label 3')
label4 = tkinter.Label(root, text='Label 4')

label1.pack()  # 打包布局,默认side=tkinter.TOP, expand=0
label3.pack(side=tkinter.RIGHT)
label2.pack(side=tkinter.LEFT)
label4.pack(side=tkinter.BOTTOM)

root.mainloop()
