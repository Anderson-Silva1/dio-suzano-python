#  Interações com o usuário

# 1. Input: Receber dados do usuário
# 2. Print: Exibir dados para o usuário
# 3. Input e Print: Receber e exibir dados para o usuário
# 4. Input e Print: Receber e exibir dados para o usuário com formatação
# 5. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo
# 6. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo (float)
# 7. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo (int)
# 8. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo (int) e (float)


# 1. Input: Receber dados do usuário
nome = input("Digite seu nome: ")

# 2. Print: Exibir dados para o usuário
print("Olá, " + nome + "!")
print("Bem-vindo ao nosso programa!")

# 3. Input e Print: Receber e exibir dados para o usuário
idade = input("Digite sua idade: ")
print("Você tem " + idade + " anos.")

# 4. Input e Print: Receber e exibir dados para o usuário com formatação
idade = input("Digite sua idade: ")
print(f"Você tem {idade} anos.")

# 5. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo
idade = int(input("Digite sua idade: ")) 
print(f"Você tem {idade} anos.")

# 6. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo (float)
altura = float(input("Digite sua altura em metros: "))
print(f"Sua altura é {altura} metros.")

# 7. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo (int)
peso = int(input("Digite seu peso em kg: "))
print(f"Seu peso é {peso} kg.")

# 8. Input e Print: Receber e exibir dados para o usuário com formatação e conversão de tipo (int) e (float)
peso = int(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}.")


# Usando o print

# 1. Print: Exibir dados para o usuário
print("Olá, mundo!")
print("Bem-vindo ao nosso programa!")

# Usando o (sep, end, flush, file, type, object) do print

# sep: Separador de valores
print("Olá", "mundo", sep=", ") # Olá, mundo
print("Bem-vindo", "ao", "nosso", "programa", sep="-") # Bem-vindo-ao-nosso-programa

# end: Finalizador de linha
print("Olá", end=", ") # Olá,
print("mundo") # Olá, mundo
print("Bem-vindo", end=" ") # Bem-vindo
print("ao", end=" ") # Bem-vindo ao
print("nosso", end=" ") # Bem-vindo ao nosso
print("programa") # Bem-vindo ao nosso programa

# flush: Forçar a impressão na tela
print("Olá", flush=True) # Olá
print("mundo", flush=True) # Olá mundo
print("Bem-vindo", flush=True) # Olá mundo Bem-vindo
print("ao", flush=True) # Olá mundo Bem-vindo ao
print("nosso", flush=True) # Olá mundo Bem-vindo ao nosso
print("programa", flush=True) # Olá mundo Bem-vindo ao nosso programa

# file: Especificar o arquivo de saída
print("Olá, mundo!", file=open("./002-conhecendo_a_linguagem/interacao_com_usuario/saida.txt", "w")) # Olá, mundo! (escreve no arquivo saida.txt)
print("Bem-vindo ao nosso programa!", file=open("./002-conhecendo_a_linguagem/interacao_com_usuario/saida.txt", "a")) # Bem-vindo ao nosso programa! (anexa no arquivo saida.txt)
