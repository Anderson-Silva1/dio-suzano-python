# **Métodos de Strings**

A classe `string` do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.

Em algumas linguagens manipular sequêncioa de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

## upper

Torna todas as letras maiúsculas

```py
texto = "Curso de Python pela DIO"
texto_upper = texto.upper()
print(texto_upper) # CURSO DE PYTHON PELA DIO
```

## lower

Torna todas as letras minúsculas

```py
texto = "Curso de Python pela DIO"
lower = texto.lower()
print(lower) # Curso De Python Pela Dio
```

## title

Torna todas as palavras a comecar com a letra maiúscula

```py
texto = "Curso de Python pela DIO"
texto_title = texto.title()
print(texto_title) # Curso De Python Pela Dio
```

## strip

Apagar os espaços em branco na direita e na esquerda do texto ou frase

```py
texto = "        Curso de Python pela DIO       "
texto_strip = texto.strip()
print(texto_strip) # Curso de Python pela DIO
```

## lstrip

Remove os espaços exedentes do lado esquerdo

```py
texto = "     Curso de Python pela DIO     "
texto_lstrip = texto.lstrip()
print(texto_lstrip) # Curso de Python pela DIO--------------

# - = espaço em branco
```

## rstrip

Torna todas as letras maiúsculas

```py
texto = "     Curso de Python pela DIO          "
texto_rstrip = texto.rstrip()
print(texto_rstrip) #      Curso de Python pela DIO
```

## center

Recebe 2 parametros, o tamanho do novo texto e do que será preenchido, ele vai pegar o texto, centralizá-lo e preencher pos espaços em branco pelo que foi programado

```py
texto = "Curso de Python pela DIO"
texto_center = texto.center(30, "-")
print(texto_center) # ---Curso de Python pela DIO---
```

## join

Uma string é na verdade uma lista, e cada caractere seria um item e possui index... O método join() recebe 2 parametros, 1. Um caractere, 2.uma lista, esse caractere vai separar cada item dessa lista pelo caractere que foi programado

```py
texto = "Python"
texto_join = ".".join(texto)
print(texto_join) # P.y.t.h.o.n
```

## replace

Substitui parte do texto

```py
texto = "Curso de Python pela DIO"
texto_replace = texto.replace("DIO", "Digital Innovation One")
print(texto_replace) # Curso de Python pela Digital Innovation One
```

## split

Separa uma um texto em uma lista de caracteres ou uma fraze em uma lista de palavras

```py
texto = "Curso de Python pela DIO"
texto_split = texto.split()
print(texto_split) # ["Curso", "de", "Python", "pela", "DIO"]
```

## upper

Torna todas as letras maiúsculas

```py
texto = "Curso de Python pela DIO"
texto_upper = texto.upper()
print(texto_upper) # CURSO DE PYTHON PELA DIO
```
