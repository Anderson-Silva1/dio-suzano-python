# **Instalação**

[Instalar GIT no WIndows](https://git-scm.com/downloads/win)

[Instalar GIT no Linux](https://git-scm.com/downloads/linux)

[Instalar GIT no MacOS](https://git-scm.com/downloads/mac)

## Configurações iniciais

### Global

```bash
git config --global user.name "<Nome do GITHUB>"
```

```bash
git config --global user.email <Email do GITHUB>
```

Você consegue ver se foi atribuído o nome e o email corretamentecomo comando

```bash
git config user.name
```

ou

```bash
git config user.email
```

Quer irá retornar o nome e o email configurado no `--GLOBAL`

### Mudando a Branch padrão para a atual

Assim conseguimos ver qual é a Branch padrão do GIT no momento

```bash
git config init.defaultBranch
```

Quando baixado o git ela vai estar na branch `master`

Mudando para branch `main`

```bash
git config --global init.defaultBranch main
```

olhando as configurações do `--global`

```bash
git config --global --list
```
