from tkinter import *

window = Tk()

window.title("Calculator")

#Global  variable for indexes
i = 0

#Number Entry
entry_number = Entry(window, font = "Calibri 20")
entry_number.grid(row = 0, column= 0, columnspan= 4, padx=5, pady=5)

#Functions
def click_button(value):
    '''Receives the value of the button'''
    global i #bring global variable i
    #Fill the entry with the value that is being written by inserting
    entry_number.insert(i, value) #We use the global index so it inserts the numbers at the index right of it
    i += 1

def erase():
    '''Delete everything from entry'''
    entry_number.delete(0, END)
    i = 0 #reinitiate global index variable

def evaluate():
    '''Evaluate what we entered'''
    equation = entry_number.get() #get the entry value
    result = eval(equation) #Evaluate the equation
    entry_number.delete(0, END) #Erase what we have
    entry_number.insert(0, result) #Insert the result
    i = 0 #reinitiate global index variable


#Buttons
button1 = Button(window, text="1", width=5, height=2, command= lambda: click_button(1))
button2 = Button(window, text="2", width=5, height=2, command= lambda: click_button(2))
button3 = Button(window, text="3", width=5, height=2, command= lambda: click_button(3))
button4 = Button(window, text="4", width=5, height=2, command= lambda: click_button(4))
button5 = Button(window, text="5", width=5, height=2, command= lambda: click_button(5))
button6 = Button(window, text="6", width=5, height=2, command= lambda: click_button(6))
button7 = Button(window, text="7", width=5, height=2, command= lambda: click_button(7))
button8 = Button(window, text="8", width=5, height=2, command= lambda: click_button(8))
button9 = Button(window, text="9", width=5, height=2, command= lambda: click_button(9))
button0 = Button(window, text="0", width=13, height=2, command= lambda: click_button(0))


button_erase = Button(window, text="AC", width=5, height=2, command=lambda: erase())
button_parenthesis_open = Button(window, text="(", width=5, height=2, command= lambda: click_button("("))
button_parenthesis_close = Button(window, text=")", width=5, height=2, command= lambda: click_button(")"))
button_decimal = Button(window, text=".", width=5, height=2, command= lambda: click_button("."))

button_div = Button(window, text="/", width=5, height=2, command= lambda: click_button("/"))
button_mult = Button(window, text="x", width=5, height=2, command= lambda: click_button("*"))
button_add = Button(window, text="+", width=5, height=2, command= lambda: click_button("+"))
button_subst = Button(window, text="-", width=5, height=2, command= lambda: click_button("-"))
button_equal = Button(window, text="=", width=5, height=2, command= lambda: evaluate())

#Button Positioning
button_erase.grid(row = 1, column = 0, padx= 5, pady=5)
button_parenthesis_open.grid(row= 1, column = 1, padx= 5, pady=5)
button_parenthesis_close.grid(row = 1, column = 2, padx= 5, pady=5)
button_div.grid(row =1, column = 3, padx= 5, pady=5)

button7.grid(row =2, column = 0, padx= 5, pady=5)
button8.grid(row =2, column = 1, padx= 5, pady=5)
button9.grid(row =2, column = 2, padx= 5, pady=5)
button_mult.grid(row =2, column = 3, padx= 5, pady=5)

button4.grid(row =3, column = 0, padx= 5, pady=5)
button5.grid(row =3, column = 1, padx= 5, pady=5)
button6.grid(row =3, column = 2, padx= 5, pady=5)
button_add.grid(row =3, column = 3, padx= 5, pady=5)

button1.grid(row =4, column = 0, padx= 5, pady=5)
button2.grid(row =4, column = 1, padx= 5, pady=5)
button3.grid(row =4, column = 2, padx= 5, pady=5)
button_subst.grid(row =4, column = 3, padx= 5, pady=5)

button0.grid(row =5, column = 0, padx= 5, pady=5, columnspan=2)
button_decimal.grid(row =5, column = 2, padx= 5, pady=5)
button_equal.grid(row =5, column = 3, padx= 5, pady=5)







window.mainloop()