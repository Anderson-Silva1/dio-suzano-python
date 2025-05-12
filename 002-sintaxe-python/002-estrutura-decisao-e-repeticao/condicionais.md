# **Estruturas Condicionais**

São estruturas que possibilitam ao códito terem escolhas, baseada no que ela foi configurada.

Elas servem como um desvio do fluxo de controle, quando determinadas expressões lógicassão atendidas

## IF

If (se) é a estrutura de condição mais simples do Python, com ela, podemos decidir, se uma condição for |True, ele será execultado:

```py
condicao = True
if condicao == True:
    print("Condição é verdadeira")

if condicao == True:
    print("Condição é falsa")
```

Ou, podemos resumir, assumindo os assuntos dos tópicos anteriores

```py
condicao = True
if condicao:
    print("Condição é verdadeira")

if not condicao:
    print("Condição é falsa")
```

Assim vemos que podemos criar vários IF's e usá-los de forma independente

## ELSE

O IF sózinho verifica a consição de forma independente, já se quisermos usar o if de 2 fatores, podemos usar o ELSE:

```py
idade = 18

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```

Perceba que usamos o `else` depois do IF e sem condição, o que significa que se o IF não satisfazer a condição desejada de `True`, ele será execultado

## ELIF

Caso duas vias de condições não seja o suficiente,podemos usar o `elif`

```py
nota = 10

if nota == 10:
    print("Exelente")
elif nota == 9:
    print("Show de bola")
elif nota == 8:
    print("Boaaa")
elif nota == 7:
    print("Razoavel")
elif nota == 6:
    print("Mediano")
elif nota < 6:
    print("Horrível")
```

Usamos 1 `IF`, 1 `ELSE` e vários `ELIF's`
