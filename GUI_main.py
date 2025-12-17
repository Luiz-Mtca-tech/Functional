from tkinter import *
from math import ceil;
import graphic.graphicGeneratorClass as graphicGeneratorClass;
#import expression.expressionGenerator as ExpressionGenerator;
import tkinter.font as TkFont;
import func.ScreenClass as ScreenClass;


class ExpressionGenerator():
    """docstring for ExpressionGenerator"""
    def readFunction(self, operation):
        pass

    def readOperation(self, operation):
        #print(f"operation size: {len(operation)}")

        final_count = []

        #percorrendo a string inteira
        #Vamos introduzir os caracteres um por um em uma lista separada.
        for x in range(len(operation)):

            # se o algarismo em questão estiver dentro
            #  lista de caracteres permitidos
            if operation[x] in self.chars:
                number = operation[x] #atribuindo o caractere a lista.
                final_count.append(number)


        #agora vamos usar essa variável para formar o números da operação
        # e converte-los para o tipo Inteiro
        number = ""

        #nessa lista vamos colocar os characteres numéricos,
        #convertidos para o tipo inteiro
        number_count = [] 
        
        #definindo o fim da lista, para servir de parâmetro no laço de repetição
        final_count.append("end")

        #Esse Loop vai percorrer a lista final_count
        #Vai coletar o caracteres numéricos e fazer a concatenação deles
        for x in range(len(final_count)):

            #se o elemento for um numero, adicione ele em nossa variável number.
            if final_count[x] in "1234567890":
                number += final_count[x]

            #caso contrário, isso indica que chegamos ao fim do numero em questão, então
            #é o momento de adicionar o que temos na nossa lista number_count.
            else:
                number_count.append(int(number)) if number != "" else number_count.append(number)
                number = "" #zera a variável number, para a próxima coleta

                #se o elemento em questão indicar alguma operação matemática, ele deve
                #ser adicionado também, mas em uma posição separada.
                if final_count[x] in "+-*^/()abcdxABCDX":
                    number_count.append(final_count[x])

        #print(f"list with strings: {final_count} ")
        #print(f"The entire list: {number_count}")
        #print(f"The sublist: {self.sublist(number_count, '(')}")/

        for value, x in enumerate(number_count):
            if value == "":
                number_count.remove(x)
            '''elif value=="(":
                pos1 = x
            elif value==")":
                print("Aqui!")
                pos2=x
                print(f"O resultado da subLista é: {self.calcOperation(number_count[pos1:pos2])}")
                #self.calcSubOperation(number_count)'''


        return number_count

    #Função recursiva para calcular as sub listas
    def nextPos(self, list, item):

        for x, val in enumerate(list):
            if val == item:
                return x

        return -1

    #Função que substitui os coefientes da função
    def replaceSubList(self, lista, value, pos1, pos2):
        
        for x, val in enumerate(lista):
            if x >= pos1 and x <= pos2:
                print(f"found! VALUE {val}, POS {x}\n")
                lista[x] = ""

        del lista[pos1:pos2]
        lista[pos1] = value
        return lista

    def calcSubOperation(self, elements):
        result2=elements
        if self.nextPos(elements, "(") != -1:

            pos1 = self.nextPos(elements, "(") + 1
            pos2 = self.nextPos(elements, ")")
        else:
            return result2
        #result é o resultado inteiro da sublista
        #realizando a conta da sublista
        result = self.calcOperation(elements[pos1:pos2])
        print(f"the type of SUBLIST: {type(elements[pos1:pos2])}")
        print(f"SUBLIST: {elements[pos1:pos2]}, POS1: {pos1}, POS2: {pos2}\n")

        #del result[pos1-1:pos2]

        #result2 é a lista com os valores devidamehte substituidos.
        #substituindo a sublista pelo seu valor
        result2 = self.replaceSubList(elements, result, pos1-1, pos2)
        print(f"SUBLIST REPLACED: {result2}\n\n\n")
        print(f"A lista sem sublista: {result2}")


        if "(" in result2:# or isinstance(result2, list):
            #pos1=self.nextPos(result2, "(")
            #pos2=self.nextPos(result2,")")
            result = self.calcSubOperation(result2)
        else:
            return result2
    


    #Essa função faz um looping que percorre a lista com os números a serem calculados, verificando os elementos
    # um por um, verificando cada operação e executando o calculo.

    def calcOperation(self, elements):
        result = 0 #resultado final
        operation = "+" #proximo tipo de operação a ser feito. Por padrão vai
                        # começar como soma para iniciar a variável result

        for item in elements:

            #se o elemento for do tipo inteiro, significa que devemos fazer uma operação
            #então vamos verificar qual ela é e executar com o número que temos até agora.
            if isinstance(item, int):
                #print("the item is Int!")
                if operation == "+":
                    result += item
                elif operation == "-":
                    result -= item
                elif operation == "*":
                    result *= item
                elif operation == "/":
                    result /= item
                elif operation == "^":
                    result = result ** item

            #se o item for do tipo string, isso quer dizer que temos uma operação para ser feita
            else:
                if item != "" : operation = item

        return result

    #Função que substitui os coeficientes pelos seus respectivos valores.
    def IndexReplace(self, number_list, x_val=2, a_val=1, b_val=1, c_val=1, d_val=1):
        
        lista = number_list

        for x in range(len(lista)):
            item = lista[x]

            if item == "a" or item == "A":
                lista[x] = a_val
            elif item == "b" or item == "B":
                lista[x] = b_val
            elif item == "c" or item == "C":
                lista[x] = c_val
            elif item == "d" or item == "D":
                lista[x] = d_val
            elif item == "x" or item == "X":
                lista[x] = x_val

        return lista

    def __init__(self):

        self.count = []
        self.chars = "1234567890+-*^/()abcdxABCDX"
        


class FunctionalWindow():

    def frame3(self):
        if not self.isOpen:
            self.frame3 = Frame(self.root, padx=10, pady=10, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)

            Entry(self.frame3, textvariable=self.a, cursor="hand2").pack(side=LEFT)
            Entry(self.frame3, textvariable=self.b, cursor="hand2").pack(side=LEFT)
            Entry(self.frame3, textvariable=self.c, cursor="hand2").pack(side=LEFT)
            Entry(self.frame3, textvariable=self.d, cursor="hand2").pack(side=LEFT)

            Button(self.frame3, text="Calc", command= lambda func=3, operation=self.personFunc.get() : self.calcFunction(func, operation)).pack()
            Button(self.frame3, text="X", bg="red", fg="white", command= lambda frame=self.frame3 : self.destroyFrame(frame)).pack()

            frame1_2 = Frame(self.frame3, padx=10, pady=10)

            Label(frame1_2, text="function(optional)").pack()
            Entry(frame1_2, textvariable=self.personFunc).pack()
            self.frame3.pack(side=TOP, fill=X)
            frame1_2.pack()
            self.isOpen = True
    def frame2(self):
        if not self.isOpen:
            self.frame2 = Frame(self.root, padx=10, pady=10, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)

            Entry(self.frame2, textvariable=self.a, cursor="hand2").pack(side=LEFT)
            Entry(self.frame2, textvariable=self.b, cursor="hand2").pack(side=LEFT)
            Entry(self.frame2, textvariable=self.c, cursor="hand2").pack(side=LEFT)

            Button(self.frame2, text="Calc", command= lambda func=2, operation=self.personFunc : self.calcFunction(func, operation)).pack()
            Button(self.frame2, text="X", bg="red", fg="white", command= lambda frame=self.frame2 : self.destroyFrame(frame)).pack()

            frame1_2 = Frame(self.frame2, padx=10, pady=10, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)

            Label(frame1_2, text="function(optional)").pack()
            Entry(frame1_2, textvariable=self.personFunc).pack()


            self.frame2.pack(side=TOP, fill=X)
            frame1_2.pack()
            self.isOpen = True

    def frame1(self):
        if not self.isOpen:
            self.frame1 = Frame(self.root, padx=10,pady=10, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
            Label(self.frame1, text="Enter the values").pack(pady=10)

            Entry(self.frame1, textvariable=self.a, cursor="hand2").pack(side=LEFT, fill=X)
            Entry(self.frame1, textvariable=self.b, cursor="hand2").pack(side=LEFT, fill=X)


            Button(self.frame1, text="Calc", command= lambda func=1, operation=self.personFunc.get() : self.calcFunction(func, operation)).pack(side=TOP)
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

        print(f"OPERATION DETECTED: {self.personFunc.get()}")
        
        graphic = graphicGeneratorClass.MathGraphi()

        match(func):
            case 1:
                print(f"1st function, values: {a}, {b}")
                image = []
                for number in [1,2,3,4,5,6]:
                    #Caso haja alguma função personalizada, vamos enviar para o enterpretador
                    # montar a conta e fazer o calculo
                    if self.personFunc.get() != "":
                        operation = self.personFunc.get()

                        #Iniciando com a Classe de leitura de funções
                        exn=ExpressionGenerator()
                        operation_list = exn.readOperation(operation)
                        operation_list = exn.IndexReplace(operation_list, number, int(a), int(b))
                        print(f"segunda etapa: {operation_list}")
                        operation_list = exn.calcSubOperation(operation_list)
                        print(f"INDEX-REPLACE: {operation_list}")
                        y = exn.calcOperation(operation_list)
                        print(f"RESULT: {y}")

                    #se não houver nenhuma função personalizada, apenas realize o modelo padrão da função.
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
                for number in [1,2,3,4,5,6]:
                    if self.personFunc.get() != "":
                        operation = self.personFunc.get()

                        exn=ExpressionGenerator()
                        operation_list=exn.readOperation(operation)
                        operation_list=exn.IndexReplace(operation_list, number, int(a), int(b), int(c))
                        operation_list=exn.calcSubOperation(operation_list)
                        y=exn.calcOperation(operation_list)

                    else:
                        y =  int(a) * (item ** 2) + (int(b) * item) + int(c);

                    #redimensionando o gráfico para caber na tela.
                    if y >= 20 or y <= -20: y = y/2;
                    image.append([number, y])

                table = graphic.generateGraph(image)

                if self.responseLabel == None:
                    self.responseLabel = Label(self.root, text=table, padx=5, pady=5)
                    self.responseLabel.pack()

                
            case 3:
                print("3th function")
                image = [];
                for number in [1,2,3,4,5,6]:
                    if self.personFunc.get() != "":
                        operation=self.personFunc.get()

                        exn = ExpressionGenerator()
                        operation_list = exn.readOperation(operation)
                        print(f"\n\n\nOperação Lida com Sucesso! {operation_list}")
                        operation_list = exn.IndexReplace(operation_list, number, int(a), int(b), int(c), int(d))
                        print(f"\n\n\nCoeficientes substituidos!{operation_list}")
                        operation_list = exn.calcSubOperation(operation_list)
                        print(f"\n\n\nSubListas calculadas! {operation_list}")

                        y = exn.calcOperation(operation_list)
                        #redimencionando o gráfico para caber na tela.
                        if y>15 or y < -15: y=ceil(y/21);
                        print(f"\n\nCONJUNTO IMAGEM DA fUNÇÃO:")
                    else:

                        x = int(x)
                        y = (int(a) * (x ** 3)) + (int(b) * (x ** 2)) - (int(c) * (x ** 1)) + int(d);
                        if y > 15 or y < -15:
                            y = ceil(y / 21);
                        image.append([x, y]);

                    image.append([number, y])

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

        self.personFunc = StringVar()
        self.custonFont = TkFont.Font(family="sans-serif", size=28)

        self.isOpen = False

        self.responseLabel = None

        self.mainWindow()
        #self.frame1()

        self.root.mainloop()


FunctionalWindow(700, 600, "Functional")