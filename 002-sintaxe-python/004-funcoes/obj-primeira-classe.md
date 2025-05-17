# **Objetos de primeira classe**

Em Python, tudo é um objeto, dessa forma funções também são objetos o que os tornam objetos de primeira classe

Com isso podemos atribuir funções à variáveis, passálas como parâmetro de uma outra função, usá-las como valores em estruturas de dados (lista, tuplas, dicionários...) e usá-la como valor de rotorn a uma outra função (closure)

```py
def exibir_resultado(num1, num2, funcao):
    resultado = funcao(num1, num2)
    return resultado

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

print(exibir_resultado(10, 20, somar))  # Saída: 30
print(exibir_resultado(10, 20, subtrair))  # Saída: -10
print(exibir_resultado(10, 20, multiplicar))  # Saída: 200
print(exibir_resultado(10, 20, dividir))  # Saída: 0.5
```
