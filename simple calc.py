from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('C:/Users/Ghanendra/Downloads/calcicon.ico')

e = Entry(root, width=40, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0, "enter your name: ") #insert name int the box having this text printed

def click(number):
   # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear():
    e.delete(0, END)

def add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def sub():
    first_num = e.get()
    global f_num
    global math
    math = "Substraction"
    f_num = int(first_num)
    e.delete(0, END)

def mul():
    first_num = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def div():
    first_num = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_num)
    e.delete(0, END)

def equal():
    second_num = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_num))

    if math == "Substraction":
        e.insert(0, f_num - int(second_num))

    if math == "Multiplication":
        e.insert(0, f_num * int(second_num))

    if math == "Division":
        e.insert(0, f_num / int(second_num))


#def button
button1 = Button(root, text="1", padx=40, pady=20, command=lambda : click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_equal = Button(root, text="=", padx=140, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=29, pady=20, command=clear)
button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
button_mul = Button(root, text="*", padx=40, pady=20, command=mul)
button_div = Button(root, text="/", padx=40, pady=20, command=div)

#button on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_equal.grid(row=6, column=0, columnspan=3)
button_add.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_sub.grid(row=5, column=0)
button_mul.grid(row=5, column=1)
button_div.grid(row=5, column=2)





root.mainloop()