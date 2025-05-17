def saudacao(name):
    return "Olá " + name

print(saudacao("Anderson"))

"""
name = Parâmetro da função

"Anderson" = Argumento da função
"""

# Return

def function(number):
    antecessor = number - 1
    sucessor = number + 1

    return antecessor, sucessor
# A função retorna uma tupla com o antecessor e o sucessor

# Argumentos
def ficha_tecnica(nome, idade, peso, profissão, sexo):
    return f"""Nome: {nome}
Idade: {idade}
Peso: {peso}
Profissão: {profissão}
Sexo: {sexo}"""


persona = {
    "nome": "Anderson",
    "idade": 30,
    "peso": 70,
    "profissão": "Programador",
    "sexo": "Masculino"
}

print(ficha_tecnica("Anderson", 30, 70, "Programador", "Masculino"))

print() # Pular linha

print(ficha_tecnica(nome = "Anderson", idade = 30, peso = 70, profissão = "Programador", sexo = "Masculino"))

print() # Pular linha

print(ficha_tecnica(**{"nome": "Anderson", "idade": 30, "peso": 70, "profissão": "Programador", "sexo": "Masculino"}))

print()

print(ficha_tecnica(**persona))
# A função retorna uma string formatada com os dados da ficha técnica