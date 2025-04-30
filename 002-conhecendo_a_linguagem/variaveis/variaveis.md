# **Variáveis**

Em linmguagem de programação podemos definir valores que podemo sofrer alteração no decorrer da execução do programa. Esses valores recebem o nome de variável, pois eles nascem com um valor e não necessáriamente vão permanecer com ele durante o programa.

## Tipagem dinâmica

Em Python, diferente do Java, C, C++ e outras linguagens, não precisamos definir o tipo de dado, o Python faz isso altomáticamente para nós, ou seja, ele associa o número 10 a classe int, e "10" a classe str, e TRUE a classe bool...

um dos grands problemas disso é que uma variável pode ter mais de um possível valor, o que pode ocasionar problemas na execulção de uma soma por exemplo, pois não será o resultado correto de 10 + "10", em Python ele vai tornar tudo uma string, ou seja, o resultado será "1010" e não 20...

## Regras de criação de variáveis

- Não pode começar com números ou caracteres especiais
- Deve seguir o padrão snake_case
- Deve ter o nome legível, o mais parecido o possível com a sua função dentro do código
- No Python não existe constantes, mas por convenção podemos criar, usando o nome da variável em caixa alta e usando o padrão snake_case

## Usando f'string

```python
nome = "Anderson"
idade = 20
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

```python
a = 5
b = 3
print(f"A soma de {a} + {b} é {a + b}")
```

```python
from datetime import datetime

data = datetime.now()
print(f"Hoje é {data:%d/%m/%Y} e agora são {data:%H:%M}")
```

```python
pi = 3.14159265
print(f"O valor de pi é {pi:.2f}")
```
