# **Parâmetros Especiais**

Como vimos, podemos passar argumentos nomeados e por posição

> ### Nomeados
>
> Nomeados é quando ele vem com o nome de identificação
>
> ### Posição
>
> Posição é quando eu tenho meus parâmetros apenas por seus índices

Mas podemos especificar isso

## Parâmetros por posição (Positional Only)

Quando eu quiser parâmetros por posição eu devop usar o caractere "\" no final de todos os parâmetros como um dos parâmetros, exemplo:

```py
def carro(marca, modelo, ano, /, cor, pais):
    print(marca, modelo, ano, cor, pais)

carro("Fusca", "Volkswagen", 1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro("Fusca", "Volkswagen", 1970, "vermelho", "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro(marca = "Fusca", modelo = "Volkswagen", ano=  1970, cor = "vermelho", pais = "Brasil") # TypeError: carro() got some positional-only arguments passed as keyword arguments: 'marca, modelo, ano'
```

Perceba que `cor` e `país` estão depois da barra, o que significa que ele não necessariamente precisam ser argumentos posicionais

## Argumentos nomeados

Para usarmos apenas argumentos nomeados, precisamos usaro caractere "\*", e tudo que tiver depois dele, deve ser passado como argumento nomeado, exemplo:

```py
def carro(marca, modelo, ano, *, cor, pais):
    print(marca, modelo, ano, cor, pais)

carro("Fusca", "Volkswagen", 1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro("Fusca", "Volkswagen", 1970, "vermelho", "Brasil") # TypeError: carro() takes 3 positional arguments but 5 were given

carro(marca = "Fusca", modelo = "Volkswagen", ano=  1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil
```

Percaba que apenas `cor` e `país` estão depois do "\*", logo apenas esses deve ser argumentos nomeados por obrigação, o restante pode ser argumento posicional ou argumento nomeado que o Python vai execultar

## Usando as duas formas

```py
def carro(marca, modelo, ano, /, *, cor, pais):
    print(marca, modelo, ano, cor, pais)

carro("Fusca", "Volkswagen", 1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro("Fusca", "Volkswagen", 1970, "vermelho", "Brasil") # TypeError: carro() takes 3 positional arguments but 5 were given

carro(marca = "Fusca", modelo = "Volkswagen", ano=  1970, cor = "vermelho", pais = "Brasil") # TypeError: carro() takes 3 positional arguments but 5 were given
```
