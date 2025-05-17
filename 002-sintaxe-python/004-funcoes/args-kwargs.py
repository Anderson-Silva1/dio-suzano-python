def poema(data_time, *args, **kwargs):
    verso = "\n".join(args)
    
    meta_dados = "\n".join({f'{chave.capitalize()}: {valor}' for chave, valor in kwargs.items()})

    message = f"{data_time}\n\n{verso}\n\n{meta_dados}"
    print(message)

poema(
    "2023-10-01",
    "A vida é bela",
    "A vida é uma flor",
    "A vida é um sonho",
    "A vida é um desafio",
    tema="Vida",
    estilo="Romântico",
    autor="Autor Desconhecido",
    ano=2023,)
    

# Saída:
# 2023-10-01
# A vida é bela
# A vida é uma flor
# A vida é um sonho
# A vida é um desafio
# Tema: Vida
# Estilo: Romântico
# Autor: Autor Desconhecido
# Ano: 2023

# Explicação:
# - A função `poema` recebe um argumento obrigatório `data_time`, seguido de um número variável de argumentos posicionais (`*args`) e um número variável de argumentos nomeados (`**kwargs`).
# - Os versos do poema são passados como argumentos posicionais e são unidos em uma única string com quebras de linha.