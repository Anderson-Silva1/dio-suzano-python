# **Fatiamento de string**

É uma técnica ultilizada para retoanar substrings (parte da string original) informando o Início (start), Fim (stop) e o Passo (step)

## Usaremos

Usaremos essa variável

```py
nome = "Estudo Python 2025"
```

## Selecionando uma letra

```py
print(nome[0])
```

No caso selecionamos o primeiro index da string

## Selecionando toda a string

```py
print(nome[::])
```

Dessa forma não definimos o start, nem o stop e nem o step, então foi mostrado tudo

## Selecionando do início

```py
print(nome[:7:])
# ou
print(nome[0:7:])
```

Estamos colocando 0 ou não limitando o start, e colocamos limite no stop

## Selecionando do meio

```py
print(nome[7::])
print(nome[7:])
```

## Selecionando tudo usando o step de 2

```py
print(nome[::2])
print(nome[0::2])
```

## Selecionando tudo ao contrário

```py
print(nome[::-1])
```
