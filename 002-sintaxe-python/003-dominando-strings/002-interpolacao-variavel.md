# **Interpolação de string**

Em Python temos 3 formas de interpolar variáveis em strings, a primeiro é usando o sinal de porcentagem (%), a segunda é usando o método format, e a última é usando o f'string

A primeiro forma (%) não é mais recomendada no Python 3 devido a sua complexidade.

## **%** (Old Style)

É uma das formas de concatenar variáveis e textos em Python, nela usamos 3 representações:

1. `%s` para string

2. `%d` para números inteiros

3. `%f` para números de pontos flutuantes

```py
nome = "Anderson"
idade = 20

print("Olá!, eu me chamo %s, tenho %d anos", nome, idade)

# >>> Olá!, eu me chamo Anderson, tenho 20 anos
```

Dessa forma não conseguimos reultilizar nada, é tudo sequencial

## Método Format

É mais simples, onde usamos chaves para colocar as variáveis. Ela pode ser usada sequencialmente, porém podemos definir um index para determinada variável

Usando modo sequencial:

```py
nome = "Anderson"
idade = 20

print("Olá!, eu me chamo {}, tenho {} anos".format(nome, idade))

# >>> Olá!, eu me chamo Anderson, tenho 20 anos
```

modo index:

```py
nome = "Anderson"
idade = 20

print("Olá!, eu me chamo {0}, tenho {1} anos".format(nome, idade))
# >>> Olá!, eu me chamo Anderson, tenho 20 anos

# Podemos usar números de pontos flutuantes para aparecer de forma agradável ao usuário

print("Olá!, eu me chamo {0}, tenho {1:.2f} anos".format(nome, idade))
```

Podemos também usar po próprio nome da variável, só que daí teremos que especificar o nome dela dentro do texto e como variável

```py
nome = "Anderson"
idade = 20

print("Olá!, eu me chamo {nome}, tenho {idade} anos".format(nome = nome, idade = idade))
# >>> Olá!, eu me chamo Anderson, tenho 20 anos
```

Podemos usar dicionários

```py
pessoa = {
"nome": "Anderson",
"idade": 20
}
print("Olá!, eu me chamo {nome}, tenho {idade} anos".format(**pessoa))
# >>> Olá!, eu me chamo Anderson, tenho 20 anos
```

## f'string

Essa é outra forma de interpolar variáveis em Python, com ela podemos usar diretamente a variável dentro da string, porém usamos a letra "f" na frente da string e as variáveis entre colchetes

```py
nome = "Anderson"
idade = 20

print(f"Olá me chamo {nome} e tenho {idade} anos de idade.")
```

Dessa forma fica mais legível e fácil de escrever, fica similar ao template string do JavaScript
