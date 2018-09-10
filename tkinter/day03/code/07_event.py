# 07_event.py


import tkinter
root = tkinter.Tk()

def mouseDownEvent(e):
    print("鼠标左键按下, 在:",
        e.x, e.y, e.x_root, e.y_root)

def mouseUPEvent(e):
    print("鼠标左键抬起")

def keyDown(e):
    print("有按键按下")

def keyUp(e):
    print("有按键抬起")

root.bind('<Button-1>', mouseDownEvent)
root.bind('<ButtonRelease-1>', mouseUPEvent)
root.bind('<KeyPress-a>', keyDown)
root.bind('<KeyRelease-a>', keyUp)


root.mainloop()
