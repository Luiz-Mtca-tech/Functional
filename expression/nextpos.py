def nextPos(lista, item):
	
	for x, val in enumerate(lista):
		if val == item:
			print("found one!")
			lista[x] = ""
			del lista[x]
			nextPos(lista, "(")
			

	return lista


print(nextPos([1,2,3,'(',54, 23, "21", ')', '3', '0', '(',24], '('));