from abc import ABC, abstractmethod
from tkinter import *

class ScreenClass(ABC):
	
	@abstractmethod
	def placeElements(self):
		pass
	
	@abstractmethod
	def calcFunction(self):
		pass
		
	def destroyWindow(self, frame):
                frame.destroy()
                if self.responseLabel != None:
                        self.responseLabel.destroy()
                        self.responseLabel = None
                self.isOpen = False

class FirstFuncClass(ScreenClass):
         
        def __init__(self, root):
                self.root = root

        def placeElements(self):
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
                #self.isOpen = True
			

        def calcFunction(self, a=1, b=1, c=0, d=0):
                return (int(a) * number) + int(b)
