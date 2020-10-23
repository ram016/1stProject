from tkinter import *
import math
root = Tk()
root.title("Calculator")

operator = ""
text_Input = StringVar()

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(root, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=3, bg="gainsboro",
                   justify='right')
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, '0')

button7 = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="7",
                 command=lambda: btnClick(7))
button7.grid(row=1, column=0)

button8 = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="8",
                 command=lambda: btnClick(8))
button8.grid(row=1, column=1)

button9 = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="9",
                 command=lambda: btnClick(9))
button9.grid(row=1, column=2)

buttonAdd = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="+",
                   command=lambda: btnClick("+"))
buttonAdd.grid(row=1, column=3)
#####################################################################################################

button4 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4",
                 command=lambda: btnClick(4))
button4.grid(row=2, column=0)

button5 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",
                 command=lambda: btnClick(5))
button5.grid(row=2, column=1)

button6 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6",
                 command=lambda: btnClick(6))
button6.grid(row=2, column=2)

buttonSub = Button(root, padx=16, pady=16, bd=8, fg="black", bg="Powder blue", font=('arial', 20, 'bold'), text="-",
                   command=lambda: btnClick("-"))
buttonSub.grid(row=2, column=3)
##################################################################################################

button1 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1",
                 command=lambda: btnClick(1))
button1.grid(row=3, column=0)

button2 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2",
                 command=lambda: btnClick(2))
button2.grid(row=3, column=1)

button3 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3",
                 command=lambda: btnClick(3))
button3.grid(row=3, column=2)

buttonMul = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="*",
                   command=lambda: btnClick("*"))
buttonMul.grid(row=3, column=3)
#####################################################################################################

button0 = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="0",
                 command=lambda: btnClick(0))
button0.grid(row=4, column=0)

buttonClr = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="C",
                   command=lambda: btnClear())
buttonClr.grid(row=4, column=1)

buttonEqu = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="=",
                   command=lambda: btnEquals())
buttonEqu.grid(row=4, column=2)

buttonDiv = Button(root, padx=16, pady=16, bd=8, bg="Powder blue", fg="black", font=('arial', 20, 'bold'), text="/",
                   command=lambda: btnClick("/"))
buttonDiv.grid(row=4, column=3)

root.mainloop()