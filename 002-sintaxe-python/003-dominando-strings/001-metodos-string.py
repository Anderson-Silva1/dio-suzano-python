texto = "Curso de Python pela DIO"
texto_c_espaco = "         Curso de Python pela DIO (com espaços)         "

print(texto.upper())  # Converte o texto para letras maiúsculas
print(texto.lower())  # Converte o texto para letras minúsculas
print(texto.title())  # Converte a primeira letra de cada palavra para maiúscula
print(texto.capitalize())  # Converte a primeira letra do texto para maiúscula
print(texto_c_espaco.strip())  # Remove espaços em branco do início e do fim do texto
print(texto.lstrip())  # Remove espaços em branco do início do texto
print(texto.rstrip())  # Remove espaços em branco do fim do texto
print(texto.replace("DIO", "Digital Innovation One"))  # Substitui "DIO" por "Digital Innovation One"
print(texto.split())  # Divide o texto em uma lista de palavras
print(texto.split(" "))  # Divide o texto em uma lista de palavras, usando espaço como delimitador
print(texto.split(" ", 2))  # Divide o texto em uma lista de palavras, usando espaço como delimitador, limitando a 2 divisões
print(texto.find("Python"))  # Retorna o índice da primeira ocorrência de "Python"
print(texto.find("Java"))  # Retorna -1 se "Java" não for encontrado
print(texto.index("Python"))  # Retorna o índice da primeira ocorrência de "Python" 
# Se não encontrado, gera um erro

print(texto.count("o"))  # Conta o número de ocorrências de "o" no texto
print(texto.count("o", 0, 10))  # Conta o número de ocorrências de "o" no texto entre os índices 0 e 10
print(texto.startswith("Curso"))  # Verifica se o texto começa com "Curso"
print(texto.endswith("DIO"))  # Verifica se o texto termina com "DIO"   

print(texto.center(50, "#"))  # Centraliza o texto em uma largura de 50 caracteres, preenchendo com "#"
print(texto.zfill(50))  # Preenche o texto com zeros à esquerda até atingir uma largura de 50 caracteres
print(texto_c_espaco.strip().center(50, "#"))  # Centraliza o texto com espaços removidos em uma largura de 50 caracteres, preenchendo com "#"