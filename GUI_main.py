from tkinter import *
from math import ceil
import graphic.graphicGeneratorClass as graphicGeneratorClass
import expression.expressionGenerator as expressionGenerator
import tkinter.font as TkFont


class FunctionalWindow():

    def frame3(self):
        if not self.isOpen:
            self.frame3 = Frame(self.root, padx=10, pady=10, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)

            Entry(self.frame3, textvariable=self.a, cursor="hand2").pack(side=LEFT)
            Entry(self.frame3, textvariable=self.b, cursor="hand2").pack(side=LEFT)
            Entry(self.frame3, textvariable=self.c, cursor="hand2").pack(side=LEFT)
            Entry(self.frame3, textvariable=self.d, cursor="hand2").pack(side=LEFT)

            Button(self.frame3, text="Calc", command= lambda func=3 : self.calcFunction(func)).pack()
            Button(self.frame3, text="X", bg="red", fg="white", command= lambda frame=self.frame3 : self.destroyFrame(frame)).pack()

            self.frame3.pack(side=TOP, fill=X)
            self.isOpen = True
    def frame2(self):
        if not self.isOpen:
            self.frame2 = Frame(self.root, padx=10, pady=10, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)

            Entry(self.frame2, textvariable=self.a, cursor="hand2").pack(side=LEFT)
            Entry(self.frame2, textvariable=self.b, cursor="hand2").pack(side=LEFT)
            Entry(self.frame2, textvariable=self.c, cursor="hand2").pack(side=LEFT)

            Button(self.frame2, text="Calc", command= lambda func=2 : self.calcFunction(func)).pack()
            Button(self.frame2, text="X", bg="red", fg="white", command= lambda frame=self.frame2 : self.destroyFrame(frame)).pack()

            self.frame2.pack(side=TOP, fill=X)
            self.isOpen = True

    def frame1(self):
        if not self.isOpen:
            self.frame1 = Frame(self.root, padx=10,pady=10, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
            Label(self.frame1, text="Enter the values").pack(pady=10)

            Entry(self.frame1, textvariable=self.a, cursor="hand2").pack(side=LEFT, fill=X)
            Entry(self.frame1, textvariable=self.b, cursor="hand2").pack(side=LEFT, fill=X)


            Button(self.frame1, text="Calc", command= lambda func=1, operation=self.personFunc : self.calcFunction(func, operation)).pack(side=TOP)
            Button(self.frame1, text="X", bg="red", fg="white", command= lambda frame=self.frame1 : self.destroyFrame(frame)).pack(side=TOP)

            frame1_2 = Frame(self.frame1, padx=5, pady=5)

            Label(frame1_2, text="Function(Optional):").pack()

            Entry(frame1_2, textvariable=self.personFunc, cursor="hand2").pack()

            self.frame1.pack(side=TOP, fill="x")
            frame1_2.pack()
            self.isOpen = True
        

    def mainWindow(self):
        Label(self.root, text="Welcome to Functional!", font=self.custonFont).pack()

        self.panel = Frame(self.root, padx=5, pady=5, highlightbackground="#26307E", highlightcolor="#32526E", highlightthickness=3, bg="#41688A")
        Button(self.panel, text="1st", width=20, height=2, bg="#7CB3C5", command=self.frame1).pack(side=LEFT, expand=True, fill="both")
        Button(self.panel, text="2sd", width=20, height=2, bg="#7CB3C5", command=self.frame2).pack(side=LEFT, expand=True, fill="both")
        Button(self.panel, text="3tr", width=20, height=2, bg="#7CB3C5", command=self.frame3).pack(side=LEFT, expand=True, fill="both")

        self.panel.pack(padx=15, pady=20, fill="x")
    def calcFunction(self, func, operation=None):
        a = self.a.get()
        b = self.b.get()
        c = self.c.get()
        d = self.d.get()
        
        graphic = graphicGeneratorClass.MathGraphi()

        match(func):
            case 1:
                print(f"1st function, values: {a}, {b}")
                image = []
                for number in [1,2,3,4,5,6]:
                    if operation != "":
                        
                        expression = expressionGenerator()
                        operation_list = expression.readOperation(operation)
                        operation_list = expression.IndexReplace(operation_list,number, self.a, self.b)
                        y = expression.calcFunction(operation_list)

                    else:
                        y = (int(a) * number) + int(b)

                    image.append([number, y])
                print(f"the image list is: {image}")
                table = graphic.generateGraph(image)
                if self.responseLabel == None:
                    self.responseLabel = Label(self.root, text=table, padx=5, pady=5)
                    self.responseLabel.pack()
                

            case 2:
                print("2sd function")
                image = []
                for item in [1,2,3,4,5,6]:
                    y =  int(a) * (item ** 2) + (int(b) * item) + int(c);
                    image.append([item, y])

                table = graphic.generateGraph(image)

                if self.responseLabel == None:
                    self.responseLabel = Label(self.root, text=table, padx=5, pady=5)
                    self.responseLabel.pack()
                
            case 3:
                print("3th function")
                image = [];
                for x in [1,2,3,4,5,6]:
                    x = int(x)
                    y = (int(a) * (x ** 3)) + (int(b) * (x ** 2)) - (int(c) * (x ** 1)) + int(d);
                    if y > 15 or y < -15:
                        y = ceil(y / 21);
                    image.append([x, y]);

                print(image)
                table = graphic.generateGraph(image)

                if self.responseLabel == None:
                    self.responseLabel = Label(self.root, text=table, padx=5, pady=5)
                    self.responseLabel.pack()

    def destroyFrame(self, frame):
        frame.destroy()
        if self.responseLabel != None:
            self.responseLabel.destroy()
            self.responseLabel = None
        self.isOpen = False
    def __init__(self, wd, hg, title):
        self.root = Tk()
        #self.root.geometry(f"{wd}x{hg}")
        self.root.title(title)
        self.root.configure(bg="#C1C1C1", padx=20, pady=20)

        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.d = StringVar()

        self.personFunc = ""
        self.custonFont = TkFont.Font(family="sans-serif", size=28)

        self.isOpen = False

        self.responseLabel = None

        self.mainWindow()
        #self.frame1()

        self.root.mainloop()


FunctionalWindow(700, 600, "Functional")