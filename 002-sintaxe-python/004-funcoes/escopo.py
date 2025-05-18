# Variável de escopo global
salario = 1518

# Função que altera a variável global
def aumento():
    global salario
    # A variável salario é global, então podemos alterá-la
    salario += 2000
    print(f'Salário dentro da função: {salario}')

print(f'Salário antes da função: {salario}')
aumento()

def sem_global():
    salario += 2000
    print(f'Salário dentro da função: {salario}')

sem_global()
# UnboundLocalError: cannot access local variable 'salario' where it is not associated with a value

# Ou seja, se não usar a palavra-chave global, o Python vai considerar que a variável salario é local e não global.
    