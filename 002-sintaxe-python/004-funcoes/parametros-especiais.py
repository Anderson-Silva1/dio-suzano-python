# Argumento posicional
def carro(marca, modelo, ano, /, cor, pais):
    print(marca, modelo, ano, cor, pais)

carro("Fusca", "Volkswagen", 1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro("Fusca", "Volkswagen", 1970, "vermelho", "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro(marca = "Fusca", modelo = "Volkswagen", ano=  1970, cor = "vermelho", pais = "Brasil") # TypeError: carro() got some positional-only arguments passed as keyword arguments: 'marca, modelo, ano'

# Argumento nomeado (keyword only)

def carro(marca, modelo, ano, *, cor, pais):
    print(marca, modelo, ano, cor, pais)

carro("Fusca", "Volkswagen", 1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro("Fusca", "Volkswagen", 1970, "vermelho", "Brasil") # TypeError: carro() takes 3 positional arguments but 5 were given

carro(marca = "Fusca", modelo = "Volkswagen", ano=  1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

# Argumento nomeado (keyword only) e posicional
def carro(marca, modelo, ano, /, *, cor, pais):
    print(marca, modelo, ano, cor, pais)    

carro("Fusca", "Volkswagen", 1970, cor = "vermelho", pais = "Brasil") # Fusca Volkswagen 1970 vermelho Brasil

carro("Fusca", "Volkswagen", 1970, "vermelho", "Brasil") # TypeError: carro() takes 3 positional arguments but 5 were given

carro(marca = "Fusca", modelo = "Volkswagen", ano=  1970, cor = "vermelho", pais = "Brasil") # TypeError: carro() takes 3 positional arguments but 5 were given


