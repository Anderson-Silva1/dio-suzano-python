# **Enviando e buscando alterações ao GITHUB**

Vamos primeiro criar um repositório local e depois um repositório no github

---

## Enviando

Ao criar nosso repositório no github, aparecerá essa mensagem

```bash
echo "# proj-repo-git-e-github" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Anderson-Silva1/proj-repo-git-e-github.git
git push -u origin main
```

Isso é basicamente o github nos ajudando

1. Iniciamos um repo local com `git init`

2. Adicionamos ao staged com `git add .`

3. Fazemos nosso commit com `git commit -m "<message>"`

4. Usamos o comando `git remote add origin <URL do nosso repositório>` para conectar nosso repo local com o repo do github

5. Rodamos o comando de envio do repo local para o servidor do github `git push -u origin main`

Com isso, já temos o nosso repositório do github recebendo os dados do nosso repositório local

## Enviando os dados ao github quando não criamos o repositório

Basta rodar o comando `git remote add origin <URL do nosso repositório>`

Rodar o comando para escolher a branche a ser linkada `git branch -M main`

E depois enviar os dados `git push -u origin main`

## Puxando dados do repositório (Ambos os casos anteriores)

Devemos nos ligar ao repositório, escolher a branch a ser usada

E quando tiver arquivos modificados no github mas não na máquina localmente, basta rodar o comando `git pull`

Esse comando vai puxar tudo do nosso repositório remoto e linkar com o nosso repositório local, tornando os dados atualizados...
