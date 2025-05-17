# **Args e Kwargs**

Podemos combinar parâmetros obrigatórios com args e kwargs.

> Parâmetros obrigatórios são aqueles parâmetros que não possuem valores padrões

Quando esses são definidos (**\*args** e **\*\*kwargs**), o método recebe os valores como Tuplas e Dicionários, respectivamente

Em Python, **\*args** e **\*\*kwargs** são formas de passar múltiplos argumentos para funções de maneira flexível.

# \*args

**\*args** permite passar vários argumentos posicionais para uma função, ou seja, valores sem nome específico.

```py
def somar(*args):
    return sum(args)

print(somar(1, 2, 3))  # Saída: 6
print(somar(10, 20))   # Saída: 30
```

## \***\*kwargs**

\***\*kwargs** permite passar vários argumentos nomeados, ou seja, pares chave = valor.

Aqui, kwargs é um dicionário: `{'nome': 'Anderson', 'idade': 21, 'curso': 'ADS'}`

Útil quando você quer passar dados opcionais e com nome.

# Resumo

| Tipo       | Símbolo    | Armazena como | Exemplo                      |
| :--------- | ---------- | ------------- | ---------------------------- |
| Posicional | \*args     | Tupla         | soma(1, 2, 3)                |
| Nomeado    | \*\*kwargs | Dicionário    | exibir(nome="Ana", idade=25) |
