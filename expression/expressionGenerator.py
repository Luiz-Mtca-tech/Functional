
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
		print(f"The entire list: {number_count}")
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
		

generator = ExpressionGenerator()

lista = generator.readOperation(input("Digite a Operação"))

print(f"Primeira Estapa:{lista}")
lista = generator.IndexReplace(lista, 2, 3, 2)
print(f"Segunda Etapa: {lista}")

lista = generator.calcOperation(lista)

print(f"FINAL RESULT: {lista}")

'''
generator = ExpressionGenerator()

lista = generator.readOperation(input("Digite a operação: "))

print(f"A lista final da função é: {lista}\n\n")


lista2 = generator.IndexReplace(lista,9, 2, 3, 1)#substituindo as incognitas e os coeficientes

lista3 = generator.calcSubOperation(lista2) #eliminando as sublistas

print(f"Letras substituídas: {lista2}\n\n")

#lista3 = generator.calcSubOperation(lista2)
print(f" O Resultado da sub-lista é {lista3}")

lista4 = generator.calcOperation(lista3)

print(f"the final result is {lista4}")'''
