from abc import ABC, abstractmethod

class ScreenClass(ABC):
	
	@abstractmethod
	def placeElements(self):
		pass
	
	@abstractmethod
	def calcFunction():
		pass
		
	def destroyWindow(self, frame):
        frame.destroy()
        if self.responseLabel != None:
            self.responseLabel.destroy()
            self.responseLabel = None
        self.isOpen = False