# **Desfazendo alterações**

## Repo git no local errado

Para resolver isso basta apagar a pasta `.git` que o git cria na incialização, e conseguimos afzer isso pelo terminal

```bash
rm -rf .git
```

Esse comando apaga a pasta `.git` e apaga nosso repositório local

## Restaurando um arquivo

No caso apagemos todo o conteúdo do nosso arquivo `README.md`, e agora?

Podemos usar o comando

```bash
git restore <nome do arquivo>
```

No nosso caso

```bash
git restore README.md
```

E nosso arquivo foi restaurado para o último commit

> OBS: Esse comando apaga toda e qualquer alteração feita localmente, pegando os dados do ultimo commit para o determinado arquivo, caso não queira descartar tudo, tome cuidado!!

## Corrigindo mensagem de commit

Conseguimos corrigir mensagens de commits quando escrevemos errado, mas apenas do ultimo `commit`

```bash
git commit --amend -m "mensagem commit modificada"
```

Dessa forma modificamos texto do ultimo commit, se rodarmos o `git log` poderemos ver isso

```bash
commit ab1213ab9dac01eba846d4258929aeb9fedfda64 (HEAD -> main)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed Apr 30 15:36:10 2025 -0300

    mensagem commit modificada
```

## Queremos agora voltar parao commit anterior, desfazendo o último

Primeiro vamos criar uma pasta chamada web, e nela vamos colocar um arquivo HTML, CSS e JavaScript

Adicionar e criar um novo commit

```bash
git add .
```

```bash
git commit -m "add pasta web"
```

No `git log` teremos

```bash
commit 6d385fc9c1564aeba4f70c887cf2137d9075c071 (HEAD -> main)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed Apr 30 16:07:07 2025 -0300

    add pasta web

commit ab1213ab9dac01eba846d4258929aeb9fedfda64
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed Apr 30 15:36:10 2025 -0300

    mensagem commit modificada
```

Dois commits

Para solucionar o problema de não querer o ultimo commit e voltar para um aterior podemos usar o

### git reset

Esse comando vai resetar nosso commit, e com ele podemos usar de 3 formas:

Antes pegamos o id do commit que queremos revogar, no nosso caso `6d385fc9c1564aeba4f70c887cf2137d9075c071`

1. `--soft`:
   Dessa forma os arquivos são enviados a area de staged

```bash
git reset --soft 6d385fc9c1564aeba4f70c887cf2137d9075c071
```

2. `--mixed`:

3. `--hard`:
