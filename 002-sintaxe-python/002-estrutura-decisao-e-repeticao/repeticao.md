# Estruturas de Repetição

São estruturas usadas para repetir um trexo de código em um determinado número de vezes.

Esse número pode ser conhecido préviamente ou determinado atravéz de uma expressão lógica

## FOR

O comando `for` é usado para percorrer um objeto iterável. Faz sentido usar ele quando saber o número exato de vezes que o código deverá ser repetido,ou quando queremos percorrer um objeto iterável.

### Estrutura do FOR

```py
nome = "Anderson"

for letra in nome:
    print(letra, end=" ") # A n d e r s o n
```

#### ELSE

Podemos usar o ELSE junto copmo for, porema função dele no for é sempre ser execultado.

```py
nome = "Anderson"

for letra in nome:
    print(letra, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")

"""
A n d e r s o n
Laço for finalizado com sucesso!
"""
```

### Função Range

Range é uma função built-in (interna) do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo).

Se usarmos `Range(i, j)` será prduzido:

```bash
i, i+2, i+3, i+4...
```

Ele recebe 3 argumentos:

1. stop (parar) - Obrigatório
2. start (início) - Opcional (padrão 0)
3. step (pulo) - Opcional (padrão 1)

## WHILE

É ultilizado para repetir um determinado bloco de código quando não sabemos quantas vezes será preciso execultar ele.

Para ele ser execultado, determinada condição ´recisa ser `True`, caso seja `False` ele sairá do while

### Estrutura do while

```py
opcao = -1

while opcao != 0:
    opcao = int(input("""
    [0] - Sair
    [1] - Sacar
    [2] - Depositar
    """))
```

### ELSE

Também podemos usar o ELSE no while, porém ele só será execultado quando o sairmos do laço do while

```py
opcao = -1

while opcao != 0:
    opcao = int(input("""
    [0] - Sair
    [1] - Sacar
    [2] - Depositar
    """))
else:
    print("Saiu do laço while com sucesso!")
```

## BREAK

Para a execulção no momento em que é chamado

```py
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")
```

## CONTINUE

Pula a execulção quando chamado

```py
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
else:
    print("\nLaço for finalizado com sucesso!")
```
