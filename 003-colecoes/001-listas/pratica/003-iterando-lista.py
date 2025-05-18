# Iterando LISTA com for
frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

for fruta in frutas:
    print(fruta)

# Usando ENUMERATE para obter o índice e o valor

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

# Usando RANGE para iterar sobre os índices
for i in range(len(frutas)):
    print(f"Índice: {i}, Fruta: {frutas[i]}")