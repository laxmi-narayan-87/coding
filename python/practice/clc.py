#create a calculator using tkinter
from tkinter import *
from tkinter import messagebox
import math
# create the main window
root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="black")
# create the entry widget
e = Entry(root, width=16, borderwidth=5, font=("Arial", 20))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# create the functions
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear():
    e.delete(0, END)
def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)
def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)
def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)
def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)
def square():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = float(first_number)
    e.delete(0, END)
def square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, END)
def power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = float(first_number)
    e.delete(0, END)
def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "square":
        e.insert(0, f_num ** 2)
    if math == "square_root":
        e.insert(0, math.sqrt(f_num))
    if math == "power":
        e.insert(0, f_num ** float(second_number))
def info():
    messagebox.showinfo("About", "This is a simple calculator created using tkinter by LAXMI NARAYAN")
# create the buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide)
button_square = Button(root, text="x^2", padx=40, pady=20, command=square)
button_square_root = Button(root, text="sqrt", padx=40, pady=20, command=square_root)
button_power = Button(root, text="x^n", padx=40, pady=20, command=power)
button_equal = Button(root, text="=", padx=40, pady=20, command=equal)
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)
button_info = Button(root, text="Info", padx=40, pady=20, command=info)
# place the buttons on the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)
button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
button_square.grid(row=5, column=0)
button_square_root.grid(row=5, column=1)
button_power.grid(row=5, column=2)
button_info.grid(row=5, column=3)
# run the main loop
root.mainloop()
