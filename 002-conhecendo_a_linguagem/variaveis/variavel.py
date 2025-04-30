# Variável

# Uma variável é um espaço na memória do computador que armazena um valor.

# O valor armazenado em uma variável pode ser alterado durante a execução do programa.

# Para criar uma variável, basta atribuir um valor a ela usando o sinal de igual (=).

# O nome da variável deve começar com uma letra ou um caractere de sublinhado (_), seguido por letras, números ou sublinhados.

# O nome da variável não pode conter espaços ou caracteres especiais, e não pode ser uma palavra reservada da linguagem.

# Exemplo de criação de variáveis

nome = "João"  # String
idade = 25  # Inteiro
altura = 1.75  # Float
peso = 70.5  # Float
ativo = True  # Booleano

# Exibindo o valor das variáveis

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Peso:", peso)
print("Ativo:", ativo)

# Alterando o valor da variável]
idade = 26  # Alterando o valor da variável idade
print("Idade alterada:", idade)

# Criando uma variável com o valor de outra variável
nova_idade = idade + 1  # Criando uma nova variável com o valor da variável idade + 1
print("Nova idade:", nova_idade)

# Criando uma variável com o valor de uma expressão
soma = idade + 5  # Criando uma nova variável com o valor da variável idade + 5
print("Soma:", soma)

# Podemos definir tipos descritivos para as variáveis, como por exemplo:
nome: str = "João"  # String
idade: int = 25  # Inteiro

# Dessa forma estamos informando ao interpretador que a variável nome é do tipo string e a variável idade é do tipo inteiro.
# Isso ajuda na legibilidade do código e pode ajudar o interpretador a identificar erros de tipo mais facilmente.
# Não mudará absolutamente nada no funcionamento do código, mas é uma boa prática de programação.
# Além disso, podemos usar o comando type() para verificar o tipo de uma variável.

print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>

# Podemos também usar o comando dir() para verificar os métodos disponíveis para uma variável.
print(dir(nome))  # Mostra os métodos disponíveis para a variável nome
print(dir(idade))  # Mostra os métodos disponíveis para a variável idade

# Podemos usar o comando help() para verificar a documentação de um método.
print(help(nome.upper))  # Mostra a documentação do método upper() da variável nome

# Podemos usar o comando id() para verificar o endereço de memória da variável.
print(id(nome))  # Mostra o endereço de memória da variável nome
print(id(idade))  # Mostra o endereço de memória da variável idade

# Podemos usar o comando del() para deletar uma variável.
del nome  # Deleta a variável nome
print(nome)  # Erro: NameError: name 'nome' is not defined

# Podemos usar o comando globals() para verificar as variáveis globais do programa.
print(globals())  # Mostra as variáveis globais do programa

# Podemos usar o comando locals() para verificar as variáveis locais do programa.
print(locals())  # Mostra as variáveis locais do programa

# Podemos usar o comando exec() para executar um código Python em forma de string.
exec("print('Olá, mundo!')")  # Executa o código Python em forma de string

# Podemos usar o comando eval() para avaliar uma expressão Python em forma de string.
print(eval("2 + 2"))  # Avalia a expressão Python em forma de string e imprime o resultado  # 4

# Podemos usar o comando compile() para compilar um código Python em forma de string.
print(compile("print('Olá, mundo!')", "<string>", "exec"))  # Compila o código Python em forma de string e imprime o resultado

# Podemos usar o comando exec() para executar o código Python compilado.
exec(compile("print('Olá, mundo!')", "<string>", "exec"))  # Executa o código Python compilado e imprime o resultado

# Podemos criar constantes em Python, que são variáveis que não podem ser alteradas durante a execução do programa.
# Para isso, basta usar letras maiúsculas para o nome da variável.
# Exemplo de criação de constantes
PI = 3.14  # Constante

print(f"PI:, {PI}")  # Exibindo o valor da constante PI

PI = 32  # Alterando o valor da constante PI (não é uma boa prática, mas é possível)

print("PI alterado:", PI)  # Erro: TypeError: 'float' object is not callable
# PI = 3.14159  # Erro: TypeError: 'float' object is not callable   

# padrão snake_case para variáveis e funções
# padrão PascalCase para classes
# padrão UPPER_SNAKE_CASE para constantes
# padrão camelCase para variáveis e funções (não é uma boa prática, mas é possível)
# padrão lowerCamelCase para variáveis e funções (não é uma boa prática, mas é possível)
# padrão UPPER_CAMEL_CASE para classes (não é uma boa prática, mas é possível)
# padrão lower_snake_case para variáveis e funções (não é uma boa prática, mas é possível)


# Conclusão

# Neste código, aprendemos sobre variáveis em Python, como criar, alterar e exibir seus valores.
# Também aprendemos sobre tipos de dados, como strings, inteiros, floats e booleanos.
# Além disso, aprendemos sobre boas práticas de programação, como usar nomes descritivos para variáveis e usar tipos descritivos.
# Por fim, aprendemos sobre constantes e como criar variáveis que não podem ser alteradas durante a execução do programa.
# Espero que este código tenha sido útil para você entender melhor sobre variáveis em Python.


# Fim do código
# Espero que este código tenha sido útil para você entender melhor sobre variáveis em Python.