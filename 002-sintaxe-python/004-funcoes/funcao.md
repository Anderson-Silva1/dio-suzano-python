# **Funções**

É um bloco de código identificado por nome e pode receber uma lista de parâmetros, esses parâmetros podem ter e não terem valores padões, parâmetros são representados pelos argumentos na hora de chamar a função.

---

Usr funções torna o código mais legível e possibilita o reaproveitamento de código.

---

Programar baseado em função, é o mesmo que dizer **_"Estamos programando de maneira estruturada"_**

---

## Definindo uma função

Para definir uma função em Python precisamos usar a palavra reservada `def`

```py
def function():
    pass
```

`function` aqui, seria o nome da função, e onde tem `pass` seria o que essa função vai retornar ou execultar

## Parâmetros

Parâmetros são informações que iremos usar dentro da função que será passada atravèz de argumentos ao chamar a função

```py
def saudacao(nome):
    print(nome)
```

`nome` ali em cima é o parâmetro

## Argumento

Argumento são as informações que será enviadas para ser os parâmetros de uma função

```py
def saudacao(nome):
    print(nome)

firstName = "Anderson"

saudacao(firstName)
```

`firstName` ali em cima é o argumento que será o `nome` (parâmetro) da função `saudacao`

## Argumentos nomeados

Podemos nomear argumentos

```py
def ficha_tacnica(nome, idade, peso, profissão, sexo):
    return f"""Nome: {nome}
Idade: {idade}
Peso: {peso}
Profissão: {profissão}
Sexo: {sexo}"""


persona1 = {
    "nome": "Anderson",
    "idade": 30,
    "peso": 70,
    "profissão": "Programador",
    "sexo": "Masculino"
}

print(ficha_tacnica("Anderson", 30, 70, "Programador", "Masculino"))

print() # Pular linha

print(ficha_tacnica(nome = "Anderson", idade = 30, peso = 70, profissão = "Programador", sexo = "Masculino"))

print() # Pular linha

print(ficha_tacnica("nome": "Anderson", "idade": 30, "peso": 70, "profissão": "Programador", "sexo": "Masculino"))

print()

print(ficha_tacnica(**persona))
```

Vemos que temos inúmeras formas de nomear argumentos ou simplesmente, não nome-á-los e só colocar os valores lá

## Parametros padrões

Se por algum motivo nós declararmos um parâmetro de uma função e não definilo nos argumentos, dará um erro

Para que isso não aconteça, podemos definir parâmetros padrões

Para isso usamos o operador "recebe" (=)

```py
def saudacao(nome = "Não informado"):
    print(nome)

firstName = "Anderson"

saudacao(firstName)
saudacao()
```

> No caso, se não informarmos o argumento do parâmetro nome da função saudacao ele vai atribuir ao parâmetro nome a string "Não informado"

# Retornando valores

As funlções podem retornar valores, para isso usamos a palavra reservaeda `return`

```py
def function():
    return 0
```

Se não usarmos o return dentro da função ela altomáticamente retornará `None`

> Python pode retornar mais de um valor

```py
def function(number):
    antecessor = number - 1
    sucessor = number + 1

    return antecessor, sucessor

function(20) # (19, 21)
```

Dessa forma essa função retorna uma tupla (lista que não pode ser alterada) com os valores retornados
