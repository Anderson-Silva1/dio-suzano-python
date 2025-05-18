listaModificar2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadradoPar = [numero ** 2 for numero in listaModificar2 if numero % 2 == 0]
quadradoImp = [numero ** 2 for numero in listaModificar2 if numero % 2 != 0]
print("Lista modificada (pares):", quadradoPar)
print("Lista modificada (impar):", quadradoImp)