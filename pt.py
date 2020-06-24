from tkinter import *
from math import *

root = Tk()
root.title("Calculator")

input_box = Entry(root, width=45, borderwidth=5)
input_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# This function is to insert double digit numbers
def click(number):
    current_number = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, (str(current_number) + str(number)))


# This function is to add a decimal point
def decimal():
    current_number = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, (str(current_number) + '.'))


# This function is to add two numbers
def adder():
    number_1 = (input_box.get())
    global first_number
    global math
    math = "addition"
    first_number = float(number_1)
    input_box.delete(0, END)


# This function is to subtract two numbers
def subtractor():
    number_1 = (input_box.get())
    global first_number
    global math
    math = "subtraction"
    first_number = float(number_1)
    input_box.delete(0, END)


# This function is to multiply two numbers
def multiplier():
    number_1 = (input_box.get())
    global first_number
    global math
    math = "multiplication"
    first_number = float(number_1)
    input_box.delete(0, END)


# This function is to divide two numbers
def divider():
    number_1 = (input_box.get())
    global first_number
    global math
    math = "division"
    first_number = float(number_1)
    input_box.delete(0, END)


# This function is raise a number to some power
def power():
    number_1 = (input_box.get())
    global first_number
    global math
    math = "power"
    first_number = float(number_1)
    input_box.delete(0, END)


# This function is to take the natural log of a number
def natural_log():
    number_1 = input_box.get()
    first_number = float(number_1)
    answer = log(first_number, e)
    input_box.delete(0, END)
    input_box.insert(0, answer)


# This function is to finally put the value on screen
def is_equal_to():
    if math == "addition":
        number_2 = input_box.get()
        input_box.delete(0, END)
        input_box.insert(0, first_number + float(number_2))

    elif math == "subtraction":
        number_2 = input_box.get()
        input_box.delete(0, END)
        input_box.insert(0, first_number - float(number_2))

    elif math == "multiplication":
        number_2 = input_box.get()
        input_box.delete(0, END)
        input_box.insert(0, first_number * float(number_2))

    elif math == "division":
        number_2 = input_box.get()
        input_box.delete(0, END)
        input_box.insert(0, first_number / float(number_2))

    elif math == "power":
        number_2 = input_box.get()
        input_box.delete(0, END)
        input_box.insert(0, first_number**float(number_2))


# This function is to clear the calculator
def clear():
    input_box.delete(0, END)


# Defining all the buttons
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
button_power = Button(root, text="^", padx=40, pady=20, command=power)
button_plus = Button(root, text="+", padx=40, pady=20, command=adder)
button_minus = Button(root, text="-", padx=40, pady=20, command=subtractor)
button_multiply = Button(root, text="X", padx=40, pady=20, command=multiplier)
button_divide = Button(root, text="/", padx=40, pady=20, command=divider)
button_equal = Button(root, text="=", padx=40, pady=20, command=is_equal_to)
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)
button_decimal = Button(root, text=".", padx=40, pady=20, command=decimal)
button_ln = Button(root, text="ln", padx=40, pady=20, command=natural_log)


# Putting all the buttons on the screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_power.grid(row=1, column=4)
button_decimal.grid(row=4, column=2)
button_plus.grid(row=4, column=3)
button_minus.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equal.grid(row=4, column=0)
button_clear.grid(row=6, column=1)
button_ln.grid(row=2, column=4)

root.mainloop()
