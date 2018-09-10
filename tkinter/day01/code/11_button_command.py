# 09_button_image.py
import tkinter

def onClick():
    print("'Click me!' 按钮被点击")

def fun():
    top = tkinter.Tk()
    top.mainloop()

root = tkinter.Tk()
btn = tkinter.Button(root, text='Click me!',
                     command=fun)

btn.pack()

root.mainloop()
