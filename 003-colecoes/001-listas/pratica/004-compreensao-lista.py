# forma antiva e mais verboso
listaFiltro1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
pares = []
impares = []

for numero in listaFiltro1:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números ímpares:", impares)

# forma mais simples e elegante (Comprimindo LISTAS)
listaFiltro2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

pares = [numeroPar for numeroPar in listaFiltro2 if numeroPar % 2 == 0]
impares = [numeroImp for numeroImp in listaFiltro2 if numeroImp % 2 != 0]

print("Números pares:", pares)
print("Números ímpares:", impares)

# Modificando valores de uma lista

# forma mais verbosa
listaModificar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in range(len(listaModificar1)):
    listaModificar1[numero] = listaModificar1[numero] * 2

print("Lista modificada:", listaModificar1)

# ou

listaModificar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for indice, numero in enumerate(listaModificar1):
    listaModificar1[indice] = listaModificar1[indice] * 2

print("Lista modificada:", listaModificar1)

# ou

listaModificar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for indice, numero in enumerate(listaModificar1):
    listaModificar1[indice] = listaModificar1[indice] * 2

print("Lista modificada:", listaModificar1)

# Criando nova lista baseado na principals
# forma mais verbosa

listaModificar2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = []

for numero in listaModificar2:
    quadrado.append(numero ** 2)

print("Lista modificada:", quadrado)


# Modificando valores de uma lista, criando outra da forma mais simples e elegante (Comprimindo LISTAS)

listaModificar2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadradoPar = [numero ** 2 for numero in listaModificar2 if numero % 2 == 0]
quadradoImp = [numero ** 2 for numero in listaModificar2 if numero % 2 != 0]

print("Lista modificada (pares):", quadradoPar)
print("Lista modificada (impar):", quadradoImp)