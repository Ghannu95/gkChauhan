from tkinter import *

root = Tk()

e = Entry(root, width=20, bg="skyblue")
e.pack()
e.get()
e.insert(0, "enter your name: ") #insert name int the box having this text printed

def myclick1():
    hi = "hello " + e.get() #variable
    mylable1 = Label(root, text="hello " + e.get())
    mylable2 = Label(root, text=hi)
    mylable2.pack()
    mylable1.pack()

def myclick():
    myLable = Label(root, text="clicked!!")
    myLable.pack()

mybutton1 = Button(root, text="enter", command=myclick1)
mybutton1.pack()

mybutton = Button(root, text="click here", command=myclick, fg="blue", bg="grey")
# bg = backgorund color, fg= foreground color
mybutton.pack()


root.mainloop()