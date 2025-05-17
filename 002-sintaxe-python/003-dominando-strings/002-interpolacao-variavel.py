pessoa = {
    "nome": "Anderson",
    "idade": 20,
    "altura": 1.80,
    "peso": 80,
    "nascimento": 2003,
    "nacionalidade": "brasileiro",
}

# Interpolação de variáveis

# Forma 1 - Usando o operador de concatenação
# O operador de concatenação é o mais simples, mas não é o mais eficiente.
print("Nome: " + pessoa["nome"])

# Forma 2 - Usando o método format()
# O método format() é mais eficiente e mais legível.
print("Nome: {}".format(pessoa["nome"]))

# Forma 3 - Usando f-strings (Python 3.6+)
# As f-strings são a forma mais moderna e eficiente de interpolação de strings.
print(f"Nome: {pessoa['nome']}")

# Forma 4 - Usando o método format() com chaves
# O método format() com chaves é útil quando você tem várias variáveis para interpolar.
print("Nome: %s" % pessoa["nome"])

# Forma 5 - Usando o método format() com índices
# O método format() com índices é útil quando você tem várias variáveis para interpolar.
print("Nome: {0}".format(pessoa["nome"]))

# Forma 6 - Usando o método format() com chaves nomeadas
# O método format() com chaves nomeadas é útil quando você tem várias variáveis para interpolar.
print("Nome: {nome}".format(nome=pessoa["nome"]))

# Forma 7 - Usando o método format() com dicionário
# O método format() com dicionário é útil quando você tem várias variáveis para interpolar.
print("Nome: {0[nome]}".format(pessoa))

# Forma 8 - Usando o método format() com dicionário e chaves nomeadas
# O método format() com dicionário e chaves nomeadas é útil quando você tem várias variáveis para interpolar.
print("Nome: {nome}".format(**pessoa))

# Forma 9 - Usando o método format() com dicionário e chaves nomeadas
# O método format() com dicionário e chaves nomeadas é útil quando você tem várias variáveis para interpolar.
print("Nome: {0}".format(pessoa.get("nome")))

# Forma 10 - Usando o método format() com dicionário e chaves nomeadas
# O método format() com dicionário e chaves nomeadas é útil quando você tem várias variáveis para interpolar.
# O método get() é útil quando você não tem certeza se a chave existe no dicionário.
print("Nome: {0}".format(pessoa.get("nome", "Desconhecido")))