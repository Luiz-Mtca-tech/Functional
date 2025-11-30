import graphic.graphicGeneratorClass as graphicGeneratorClass
import math

class Main():
    def firstGrade(self, a = 1, b = 0, x_list = [1,2,3]):
        image = []
        for number in x_list:
            y = (int(a) * number) + int(b)
            image.append([number, y])

        return image
        
    def secondGrade(self, a=1, b=1, c=0, x_values = [1,2,3]):    
        image = []
        for item in x_values:
            y =  int(a) * (item ** 2) + (int(b) * item) + int(c);
            image.append([item, y])

        print(f'\n\n\n\n\n\n {image}')
        return image;

    def thirdGrade(self, a=1, b=1, c=1, d=0, x_values = [1,2,3]):
        image = [];
        for x in x_values:
            x = int(x)
            y = (int(a) * (x ** 3)) + (int(b) * (x ** 2)) - (int(c) * (x ** 1)) + int(d);
            if y > 15 or y < -15:
                y = math.ceil(y / 21);
            image.append([x, y]);

        print(image)
        return image;

    def getInputs(self):
        x_list = []

        print("Do you wish to enter the values for X? Yes or No?")
        reply = input(": ")
        if(reply == "Yes" or reply == "yes" or reply == "y"):
            while(True):
                value = input("Type a number: ")
                if value == "quit" or value == "exit" or value == "stop" :
                    break
                else :
                    try:
                        x_list.append(int(value))
                    except:
                        print("only numbers are allowed!")
            
            return x_list
        else:
            return [1,2,3,4,5]

    def __init__(self):
        self.x = (-3, -2, -1, 0, 1, 2, 3)
        print("Hello World!")
        print("|----------------------------------------|")
        print("|        WELCOME TO FUNCTIONAL.PY        |")
        print("|----------------------------------------|")

        print("\n\n with which function do you want to begin?\n\n1 = 1ft;\n\n2 = 2nd;\n\n3 = 3nd\n\n")

        engine = graphicGeneratorClass.MathGraphi()

        match(int(input("Which function it will be?"))):
            case 1:
                print("First case")

                print("Now we need to know what is the follow values:")
                a = input("a: ")
                b = input("b: ")

                x = self.getInputs()
                
                result = self.firstGrade(a, b, x);
                result = engine.generateGraph(result)
                print(result)

            
            case 2:
                print("Now we need to know the values for your function")
                a = input("a: ")
                b = input("b: ")
                c = input("c: ")

                x = self.getInputs()

                result = self.secondGrade(a, b, c, x)
                result = engine.generateGraph(result)
                print(result)
                #print(f"\n\n\n {result}")


            case 3:
                print("third case!")
                a = input("a: ")
                b = input("b: ")
                c = input("c: ")
                d = input("d: ")

                x = self.getInputs()

                result = self.thirdGrade(a,b,c,d, x)
                result = engine.generateGraph(result)
                print(result)

            case _:
                pass;

Main();