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

Antes pegamos o id do commit anterior que queremos revogar, no nosso caso ` ab1213ab9dac01eba846d4258929aeb9fedfda64`

1. `--soft`:
   Dessa forma os arquivos criados e comitados nos commits posteriores são enviados a area de staged, e esses mesmos commits serão desfeitos, ou seja, não irão mais existir.

```bash
git reset --soft ab1213ab9dac01eba846d4258929aeb9fedfda64
```

2. `--mixed`:
   Este é o comportamento padrão do `git reset`, ele vai pegar as modificações e criações feitas nos commits posteriores ao que pegamos como ponto de referência e e coloca essas criações e modificações na arvore de trabalho, fora do da pasta `.git`

```bash
git reset ab1213ab9dac01eba846d4258929aeb9fedfda64
```

ou

```bash
git reset --mixed ab1213ab9dac01eba846d4258929aeb9fedfda64
```

3. `--hard`:
   Este comportamento é o mais perigoso pois ele apaga o commit por completo, ate os arquivos dele

```bash
git reset --hard ab1213ab9dac01eba846d4258929aeb9fedfda64
```

Aparacerá essa mensagem nesse modo de usar o `reset`

```bash
HEAD is now at 9f9b2f0 reset add pasta web
```

---

### Histórico detalhado

Para ver o histórico de forma detalhada, podemos usar o comando:

`git reflog`

que retornará:

```bash
9f9b2f0 (HEAD -> main) HEAD@{0}: reset: moving to 9f9b2f0a8ea79c64aa06a86f871222d3b202e9f8
2b01f66 HEAD@{1}: commit: pasta public
9f9b2f0 (HEAD -> main) HEAD@{2}: commit: reset --soft
fb95b9f HEAD@{3}: reset: moving to fb95b9fe9abc173c80d1ef81d7bacf937e5cf4e3
5bbdc2e HEAD@{4}: commit: add pasta web!
fb95b9f HEAD@{5}: commit (initial): primeiro commit
```

---

## Observações

Só dfevemos fazer esse tuipo de alteração, usando o reset quando nãoenviamos nada aio repositório remoto ainda, pois em outras máquinas que já tem o repositório clonado poderá ter conflito...

Nesse caso, o ideal pe fazer um novo commit, com as novas alterações e modificações

---

<br />
<br />
<br />
<br />

# EXTRA

Podemos tirar arquivos da area de staged usando o comando:

`git reset <caminho do arquivo>`

ou

`git restore --staged <caminho do arquivo>`
