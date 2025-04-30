# **Criando e Clonando repositórios**

Existem duas formas de obter um repositório Git na sua máquina

1. **Transformando um diretório local que não está sob um controle de versão, num repositório .GIT;**

2. **Clonando um Repositório exesitente**

## Modo 1

### Criar nossa pasta

```bash
mkdir repo-local
```

### Entrar na pasta criada

```bash
cd repo-local
```

### Inicializar repositório local

```bash
git init
```

e será rtetornado para nós o seguinte

> Initialized empty Git repository in C:/Users/noteb/repo-local/.git/

isso significa que o repositório git local foi criado com sucesso, e que uma pasta .git foi criada, e é nela que será contida todos os nossos commits

### Enviando nosso projeto ao GitHub

precisamos ter primeiro o repositório criado no github

Depois de criado, precisamos rodar o comando

```bash
git remote add origin https://github.com/Anderson-Silva1/repo-remoto.git
```

E seu repositório já estará no github

## Modo 2

### Clonar um repositório

```bash
git clone <endereço do repositório>
```

exemplo

```bash
git clone https://github.com/Anderson-Silva1/proj-imc-javascript.git
```

e será retornado uma mensagem assim

```bsh
Cloning into 'proj-imc-javascript'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (8/8), done.
```

E significa que o repositótio foi clonedo com sucesso!!

> Porem vejamos que foi clonado com o nome `proj-imc-javascript`

Podemos mudar esse nome na hora de clonar, basta adicionar o nome da pasta paraonde será clonada o projeto

```bash
git clone https://github.com/Anderson-Silva1/proj-imc-javascript.git calc-imc
```

nesse caso criou a pasta chamada `calc-imc`
