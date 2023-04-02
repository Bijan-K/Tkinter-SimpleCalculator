from tkinter import *
import operator

root = Tk()
root.title("Calculator")
root.configure(bg='#001e3b')

inputField = Entry(root, width=50, borderwidth=5)
inputField.grid(row=1,column=0,columnspan=4, padx=7,pady=(0,7))
currentNum = Label(root, fg ="white", text="-",bg='#001e3b',justify=LEFT, anchor="w")
currentNum.grid(row=0,column=0,sticky = W, padx=(2,0))

ops = {"+": operator.add, "-":operator.sub,"*":operator.mul,"/":operator.floordiv}
opsArray = []

def updateCurrentNumb(text):
    currentNum.config(text= text)

def numClickHandler(input):
        lastNum = inputField.get()
        inputField.delete(0, END)
        inputField.insert(0, lastNum + input)

def opsHandler(op):
    if(currentNum.cget("text") != '-'):
        if(inputField.get() == ''):
            updateCurrentNumb(currentNum.cget("text")[:-1] + op)
            opsArray.pop(0)
        else:
            num1 = int(inputField.get())
            num2 = int(currentNum.cget("text")[:-1])
            updateCurrentNumb(str(ops[opsArray[0]](num2,num1)) + op)
            opsArray.pop(0)
    else:
        updateCurrentNumb(inputField.get() + op)

    opsArray.append(op)
    inputField.delete(0,END)


def resultHandler():
    if(currentNum.cget("text") != '-'):
        num1 = int(inputField.get())
        num2 = int(currentNum.cget("text")[:-1])
        inputField.delete(0, END)
        inputField.insert(0, str(ops[opsArray[0]](num2,num1)))
        opsArray.pop(0)
        currentNum.config(text= "-")
    
    
def clearHandler():  
    global opsArray      
    opsArray=[]
    inputField.delete(0,END)
    currentNum.config(text= "-")


# Define buttons
button_1 = Button(root, text="1", padx=30,pady=15, command=lambda: numClickHandler('1'))
button_2 = Button(root, text="2", padx=30,pady=15, command=lambda: numClickHandler('2'))
button_3 = Button(root, text="3", padx=30,pady=15, command=lambda: numClickHandler('3'))
button_4 = Button(root, text="4", padx=30,pady=15, command=lambda: numClickHandler('4'))
button_5 = Button(root, text="5", padx=30,pady=15, command=lambda: numClickHandler('5'))
button_6 = Button(root, text="6", padx=30,pady=15, command=lambda: numClickHandler('6'))
button_7 = Button(root, text="7", padx=30,pady=15, command=lambda: numClickHandler('7'))
button_8 = Button(root, text="8", padx=30,pady=15, command=lambda: numClickHandler('8'))
button_9 = Button(root, text="9", padx=30,pady=15, command=lambda: numClickHandler('9'))
button_0 = Button(root, text="0", padx=30,pady=15, command=lambda: numClickHandler('0'))

button_add = Button(root, text="+", padx=28,pady=15,bg='#5a6470',fg='#fff', command=lambda: opsHandler("+"))
button_subtract = Button(root, text="-", padx=30,pady=15,bg='#5a6470',fg='#fff', command=lambda: opsHandler("-"))
button_multiple = Button(root, text="*", padx=30,pady=15,bg='#5a6470',fg='#fff', command=lambda: opsHandler("*"))
button_divide = Button(root, text="/", padx=30,pady=15,bg='#5a6470',fg='#fff', command=lambda: opsHandler("/"))

button_equal = Button(root, text="=", padx=30,pady=15, bg="#326da8", command=resultHandler)
button_clear = Button(root, text="C", padx=30,pady=15, bg="#bd3939", command=clearHandler)

# Place on Screen
button_9.grid(row=2,column=2,pady=2)
button_8.grid(row=2,column=1)
button_7.grid(row=2,column=0)
button_add.grid(row=2,column=3,padx=(4,0))

button_6.grid(row=3,column=2,pady=2)
button_5.grid(row=3,column=1)
button_4.grid(row=3,column=0)
button_subtract.grid(row=3,column=3,padx=(4,0))

button_3.grid(row=4,column=2,pady=2)
button_2.grid(row=4,column=1)
button_1.grid(row=4,column=0)
button_multiple.grid(row=4,column=3,padx=(4,0))

button_equal.grid(row=5,column=2,pady=2)
button_0.grid(row=5,column=1)
button_clear.grid(row=5,column=0)
button_divide.grid(row=5,column=3,padx=(4,0))


root.mainloop()