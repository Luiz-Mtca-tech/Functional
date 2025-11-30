from tkinter import *

root = Tk()
root.title("Functional.py")
root.geometry("800x700")

function1Frame = Frame(root, padx=50, pady=50, bg="white", highlightbackground="blue", highlightthickness=2, highlightcolor="black")

number1 = StringVar()

a = Label(root, text="Hello, World!")
a.pack()

Label(root, text="WELCOME TO THE FUNCTIONAL.PY").pack()

def openFunction1():
    global function1Frame
    function1Frame = Frame(root, padx=50, pady=50, bg="white", highlightbackground="gray", highlightthickness=2, highlightcolor="black")
    Entry(function1Frame, textvariable=number1, cursor="hand2").pack()

    Button(function1Frame, text="Submit", cursor="hand2", command=submit).pack()
    Button(function1Frame, text="close", command=destroyFrame, bg="red", fg="white", highlightbackground="black", highlightthickness=1).pack()


    function1Frame.place(x=50, y=300)



def destroyFrame():
    function1Frame.destroy()

def submit():
    print(number1.get())
    return number1.get()

Entry(function1Frame, textvariable=number1, cursor="hand2").pack()

Button(function1Frame, text="Submit", cursor="hand2", command=submit).pack()
Button(function1Frame, text="close", command=destroyFrame, bg="red", fg="white", highlightbackground="black", highlightthickness=1).pack()

function1Frame.place(x=50, y=300)


Button(root, text="1st Function", command=openFunction1).pack()
Button(root, text="close function", command=destroyFrame).pack()

root.mainloop()