# **Trabalhando com Branches**

De maneira simplícida, **Branch** _(Tradução: "Ramo")_, é uma ramificação do nosso projeto

- É um ponteiro móvel para um commit no histórico do repositório

- Quando iniciamos uma `Nova Branch` apartir de uma nova já existente, a `Nova` se inicia apontandopara o mesmo `Commit` da `Branch` que estava quando foi criada

---

## **Trabalhando na prática**

> Precisamos primeiro ter nosso repositório, olhe os estudos anteriores e faça o passo a passo

Depois de ter nosso repositório local, vamos fazer nosso primeiro commit com chamado "commit-0", onde terá um arquivo `README.md`

```bash
commit 541dcaa692d14ecef848cc5c281b99a068d9a2cc (HEAD -> main)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Tue May 6 10:22:13 2025 -0300

    commit-0
```

Vamos agora criar um arquivo chamado `commit-1-branch-main.txt` e daremos mais um commit, com o título `commit-1`

---

Agora vamos criar nossa Branch e chamaremos ela de `teste`, usaremos o comando:

`git checkout -b "teste"`

Usaremos agora o comando `git log`

```bash
$ git log
commit e0d2433332292c28537ef788762777b27e0376b0 (HEAD -> teste, main)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed May 7 00:27:18 2025 -0300

    commit-1

commit 541dcaa692d14ecef848cc5c281b99a068d9a2cc
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Tue May 6 10:22:13 2025 -0300

    commit-0
```

Isso nos mostra que a Branch teste já foi criada, que já estamos nela, e que o commit dela (Branch teste) aponta para o commit da Branch main também

---

Agora iremos commitar dentro da Branch teste com o título de "commit-2" e com um arquivo `commit-2-branch-teste.txt`

Se dermos o `git log` agora veremos:

```bash
$ git log
commit 1485aebfd9fe2cf6bc1a5905bc87e3f5133441ab (HEAD -> teste)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed May 7 00:35:18 2025 -0300

    commit-2

commit e0d2433332292c28537ef788762777b27e0376b0 (main)
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Wed May 7 00:27:18 2025 -0300

    commit-1

commit 541dcaa692d14ecef848cc5c281b99a068d9a2cc
Author: Anderson-Silva1 <anderson.developer360@gmail.com>
Date:   Tue May 6 10:22:13 2025 -0300

    commit-0
```

Vemos que o commit-2 está na Branch teste, e a branch main está no commit-1

---

Agora vamos mudar de Branch, para isso usamos o comando: `git checkout <nome da branch>`, no nosso caso `git checkout main`

Perceba agora que o arquivo que foi commitado apenas na branch teste (`commit-2-branch-teste.txt`), não está aparecendo na branch main, isso acontece pq o arquivo `commit-2-branch-teste.txt` só existe na branch teste

E mesmo como `git status` não é possivel visualizar ele na area de trabalho

---

### Ultimo commit de cada Branch

Podemos ver isso usando o comando `git branch -v`, e com isso temos:

```bash
* main  e0d2433 commit-1
  teste 1485aeb commit-2
```

O `*` referencia a branch que estamos, no nosso caso a main

---

### Mesclando branches

Podemos fazer isso usando o comando `git merge <nome da branch a ser mesclada>`, no nosso caso `git merge teste`

Assim, podemos rodar o comando `git branch -v` e veremos o seguinte:

```bash
* main  1485aeb commit-2
  teste 1485aeb commit-2
```

As duas Branches estão apontando para o mesmo commit, o que significa que o arquivo `commit-2-branch-teste.txt` agora está aparecendo na branch main, o que não aparecia antes

> **OBS**: Para que o comando `git merge <branch>` funcionar, precisamos estar na branch que iremos usar para mesclar a outra branch, no nosso caso a `branch main`

---

### Excluindo Branches

Depois de usar uma branch e mesclar ela com a branch principal, não usaremos mais ela, ou seja ela precisa ser deletada

Mas antes vamos listar as branches que temos usando o comado: `git branch`

```bash
* main
  teste
```

E para deletar usamos o comando: `git branch -d <nome branch a ser deletada>`, no nosso caso `git branch -d teste`

Depois de rodaro comando acima, vamos visualizar quantas branches temos no nosso projeto:

```bash
* main
```

Ou seja, temos apenas uma branch agora

---

### Deletar branch remota

Usamos o comando: `git push origin --delete <nome-da-branch>`, no nosso caso `git push origin --delete teste`

Assim conseguimos deletar nossa branch remotamente

---

### Criando uma branch remotamente

Usamos o comando: `git push -u origin <nome da branch>`, no nosso caso `git push -u origin teste`

---

## Principais comando de Branch

| Ação                          | Comando                                                          |
| :---------------------------- | :--------------------------------------------------------------- |
| Criar e trocar de branch      | `git checkout -b <nome-da-branch>`                               |
| Listar todas as branches      | `git branch`                                                     |
| Trocar de branch              | `git switch <nome-da-branch>` ou `git checkout <nome-da-branch>` |
| Deletar branch local          | `git branch -d <nome-da-branch>`                                 |
| Deletar branch remota         | `git push origin --delete <nome-da-branch>`                      |
| Subir branch para GitHub      | `git push -u origin <nome-da-branch>`                            |
| Ver todas as branches remotas | `git branch -r`                                                  |
