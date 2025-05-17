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