# **Operadores lógicos**

São operadores ultilizados em conjunto com os operadores de comparação, para montar expressões lógicas. Quando um operadorde comparação é ultilizado, o resultadoé um boleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos

### Comparação

```py
saldo = 1000
saque = 200
liite = 100

print(saldo >= saque) # True
print(saldo <= limite) # false
```

### Comparação e lógico

```py
saldo = 1000
saque = 200
liite = 100

print(saldo >= saque and saldo <= limite) # false
```

## Operadores

### and (E lógico)

Retorna `True` se ambas as expressões forem verdadeiras.

```py
a = True
b = False
resultado = a and b  # False
```

### or (OU lógico)

Retorna True se pelo menos uma das expressões for verdadeira.

```py
a = True
b = False
resultado = a or b # True
```

### not (NÃO lógico)

Inverte o valor lógico da expressão.

```py
a = True
resultado = not a # False
```
