from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/Ghanendra/Desktop/gk.ico')


my_img1 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("E:/chacha storage/image/9.jpg"))


img_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9]

status = Label(root, text="image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
#anchor : for move inside text to E or W or N or S
#bd : for border
#sticky for streach border in desired direction
#
status.grid(row=3, column=0, columnspan=3, sticky=W+E)

my_lable = Label(image = my_img1)
my_lable.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global my_lable
    global button3
    global button1


    my_lable.grid_forget()
    my_lable= Label(image=img_list[img_num-1])
    button3= Button(root, text=">>",command=lambda : forward(img_num+1))
    button1= Button(root, text="<<", command=lambda : backward(img_num-1))
    my_lable.grid(row=0, column=0, columnspan=3)

    if img_num == 9:
        button3 = Button(root, text=">>", state=DISABLED)

    button1.grid(row=1, column=0)
    button3.grid(row=1, column=2)
    status = Label(root, text="image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)


def backward(img_num):
    global my_lable
    global button3
    global button1

    my_lable.grid_forget()
    my_lable = Label(image=img_list[img_num - 1])
    button3 = Button(root, text=">>", command=lambda: forward(img_num + 1))
    button1 = Button(root, text="<<", command=lambda: backward(img_num - 1))
    my_lable.grid(row=0, column=0, columnspan=3)
    if img_num == 1:
        button1 = Button(root, text="<<", state=DISABLED)
    button1.grid(row=1, column=0)
    button3.grid(row=1, column=2)
    status = Label(root, text="image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)



#exit button
button1 = Button(root, text="<<")
button2 = Button(root, text="Exit", command=root.quit)
button3 = Button(root, text=">>", command=lambda : forward(2))
button1.grid(row=1, column=0)
button2.grid(row=1, column=1 )
button3.grid(row=1, column=2, pady=10)


root.mainloop()