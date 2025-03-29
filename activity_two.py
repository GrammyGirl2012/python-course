from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("100x180")
    top.title("toplevel")
    l2 = label(top , text = "This is top level window") 
    l2.pack()

    top.mainloop()

l = Label(root, text = "This is the root window")
btn = Button(root, text =" click here to open an another window", command = topwin)

l.pack()
btn.pack()
root.mainloop