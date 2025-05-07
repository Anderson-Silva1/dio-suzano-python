# Conversao de tipos em Python

# Inteiro para float
inteiro = 10
flutuante = float(inteiro)
print(f"Conversão de inteiro para float: {inteiro} -> {flutuante}")

# podemos fazer isso usando a divisão
inteiro = 10
flutuante = inteiro / 2

print(f"Divisão de inteiro para float: {inteiro} -> {flutuante}")

# Float para inteiro
flutuante = 10.5
inteiro = int(flutuante)

print(f"Conversão de float para inteiro: {flutuante} -> {inteiro}")

# Float para inteiro
flutuante = 10.5
inteiro = flutuante // 1  # Arredondamento para baixo
# ou podemos usar a função round() para arredondar o número
inteiro = round(flutuante)  # Arredondamento para o inteiro mais próximo
print(f"Conversão de float para inteiro com arredondamento: {flutuante} -> {inteiro}")

# numero inteiro para string
inteiro = 10
string = str(inteiro)
print(f"Conversão de inteiro para string: {inteiro} -> {string}")

# string para inteiro
string = "10"
inteiro = int(string)
print(f"Conversão de string para inteiro: {string} -> {inteiro}")

# string para float
string = "10.5"
flutuante = float(string)
print(f"Conversão de string para float: {string} -> {flutuante}")

# float para string
flutuante = 10.5
string = str(flutuante)
print(f"Conversão de float para string: {flutuante} -> {string}")

