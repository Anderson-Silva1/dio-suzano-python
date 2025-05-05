# Operadores Aritméticos em Python

Em Python temos os principais

* Soma

```py
print(1 + 1)
>>> 2
```

* Subtração

```py
print(3 - 1)
>>> 2
```

* Multiplicação

```py
print(2 * 4)
>>> 8
```

* Divisão

```py
print(10 / 2)
>>> 5.0
```

* Divisão Inteira

```py
print(10 // 5)
>>> 5
```

* Módulo (Resto)

```py
print(10 % 3)
>>> 1
```

* Exponênciação

```py
print(2 ** 3)
>>> 8
```

## Ordem de Precedência

Na matemática existe uma regra que indicam quais operações devem ser execultadas primeiro. Isso é útil pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser diferente

exemplo:

```py
print(10 - 5 * 2)
# Qual seria o resultado? 10 ou 0?
```

Nesse caso o resultado seria 0, pois a Multiplicação, na matemática possui uma procedência maior que a soma

## Sequencia de Precedência

1. ### Parênteses

    - ()
    - **MAIS ALTA PRECEDÊNCIA**: Tudo que estiver dentro de Parênteses será avaliado primeiro

2. ### Exponênciação

    - **
    - 2 ** 4 = 16

3. ### Multiplicação, Divisão e Módulo

    - *; /; %; //
    - Estes, entre eles possuem precedência igual, ou seja, quem aparecer primeiro será calculado pelo Python

1. ### Adição e Subtração

    - +; -
    - São os últimos na ordem de precedência, ou seja, tidas as outras verificações das operações acima serão execultadas primeiro que essas.