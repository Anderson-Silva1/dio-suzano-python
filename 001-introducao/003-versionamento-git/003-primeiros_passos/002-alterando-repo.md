# **Alterando e salvando alterações no repositório local**

> ## Já criou o seu repositório local? se ainda não, crie-o e volte aqui

Logo de largada quero te mostrar um comando para verificar as alterações do seu repositório

```bash
git status
```

Esse comando te mostra todas as alterações feitas, no nosso caso aparecerá essa mensagem

```bash
On branch main
No commits yet
nothing to commit (create/copy files and use "git add" to track)
```

Mostrando que não temos nenhum commit feito

---

Vamos adicionar um arquivo chamado README.md

```bash
touch README.md
```

Perceba que nosso `git status` ja mudou

```bash
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

Mostrando que temos um arquivo que foi criado mas não está salvo ou `Untracked files`, que são arquivos não rastreados pelo .git no repositório...

> Quem está fazendo essa verificação é a pasta .git do nosso repositório

---

## Staged

Staged é uma área onde ficarão nossos arquivos modificados ou não commitados

Para adicionar arquivos a essa área basta rodar o comando

```bash
git add <nome-do-arquivo>
```

No nosso caso

```bash
git add README.md
```

Perceba que jámudou nosso `git status`

```bash
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

Nos mostrando que o arquivo README.md estás na área de `staged`

> Seguindo essa forma, deveríamos colocar cada arquivo por vêz no staged, mas quando se trata de muitos arquivos, isso se torna inviável, para isso temos um comando:

```bash
git add .
```

> Esse comando pega tudo que foi modificado e criado e manda ao `staged`

## Commit

Commit é a ação usada para salvar arquivos em um repositório

```bash
git commit -m "<mensagem do commit>"
```

no nosso caso

```bash
git commit -m "first commit"
```

Esse comando vai pegar tudo que está no `staged` e vai salvar no repositório

Aparecerá essa mensagem

```bash
[main (root-commit) 57cfa0b] first commit
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```

Isso mostra o que foi adicionado e modificado...

## git log

`git log` vai nos mostrar todos os nossos commit do nosso repositório

```bash
commit 57cfa0be14f37f462c54d66c667364dc7d42ed5f (HEAD -> main)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed Apr 30 15:36:10 2025 -0300

    first commit
```

Em `commit` nós temos o endereço do commit, se quisermos achar ele, esse é o código

Em `Author` temos informações sobre o autor do commit, como nome e email configurados no `--global`

Em `Date` temos as informações de criação do commit, como hora e dia, ano...

---

Se rodarmos o `git status` veremos que

```bash
On branch main
nothing to commit, working tree clean
```

Não temos mais arquivos não rastreados ou modificados

## Pastas vazias

O git não reconhece pastas vazias, mas para adicionar pastas vazias dentro do repositório usamos uma convenção onde temos o arquivo `.gitkeep` dentro dessa pasta
