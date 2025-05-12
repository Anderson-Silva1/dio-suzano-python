### Usando IF
condicao = True

if condicao:
    print("A condição é verdadeira")

if not condicao:
    print("A condição é falsa")

### Usando ELSE

idade = 18

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

### Usando ELIF

nota = 10

if nota == 10:
    print("Exelente")
elif nota == 9:
    print("Show de bola")
elif nota == 8:
    print("Boaaa")
elif nota == 7:
    print("Razoavel")
elif nota == 6:
    print("Mediano")
elif nota < 6:
    print("Horrível")

###

# If aninhado

if nota >= 7:
    if nota == 10:
        print("Exelente")
    elif nota == 9:
        print("Show de bola")
    elif nota == 8:
        print("Boaaa")
    elif nota == 7:
        print("Razoavel")
else:
    if nota == 6:
        print("Mediano")
    elif nota < 6:
        print("Horrível")

###