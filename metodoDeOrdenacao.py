def sortByMe(numeros):
	for num in numeros:
		x=0;y=x+1
		while len(numeros) > y:
			if numeros[x] > numeros[y]:
				a = numeros[x]
				numeros[x] = numeros[y]
				numeros[y] = a
			x += 1; y += 1
	return numeros