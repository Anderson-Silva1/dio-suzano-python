# **Identacao**

## Estética

Isentar o código é uma forma de manter o código fonte mais legível e manutenivel

Mas em Lython, ela (identacao) exerce um segundo papel, através da identacao o interpretador Python consegue determinar onde um bloco de código inicia e quando esse mesmo bloco de código finaliza

## Blocos de comando

As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar o início e o fim de um bloco de código, em Java, C e JavaScript (que deriva do C) usam as `chaves`:

### Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```

### C

```c
#include <stdio.h>

int main() {
    printf("Olá, mundo!\n");
    return 0;
}
```

### JavScript

```js
console.log("Olá, mundo!");
```

## Utilizando espaços

Existe uma convenção em Python, que define boas práticas Lara escrita de código na linguagem. 

Neste documento é indicado usar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos na linha a baixo 4 novos espaços em branco a mais.