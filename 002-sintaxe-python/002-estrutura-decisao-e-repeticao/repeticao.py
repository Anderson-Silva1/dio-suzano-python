# for

nome = "Anderson"

for letra in nome:
    print(letra, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")

""" EXECUÇÃO
A n d e r s o n 
Laço for finalizado com sucesso!
"""

# Range

numero = 5

lista = range(0, 51, numero)
# range(inicio, fim, passo)
# range(0, 51, 5) = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for numero in lista:
    print(numero, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")

"""
0 5 10 15 20 25 30 35 40 45 50 
Laço for finalizado com sucesso!
"""

# while

opcao = -1

while opcao != 0:
    opcao = int(input("""
    [0] - Sair
    [1] - Sacar
    [2] - Depositar
    """))
else:
    print("Saiu do laço while com sucesso!")

# Usando break e continue

# break

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")

""" 
0 1 2 3 4
Laço for finalizado com sucesso!
"""

# continue

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")

"""
0 1 2 3 4 6 7 8 9
Laço for finalizado com sucesso!
"""

# Laço infinito

# while True:
#     print("Laço infinito")
#     break
#     print("Laço infinito")
# else:
#     print("Saiu do laço while com sucesso!")

