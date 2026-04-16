# Questão 09

Uma matriz 2x2 pode ser representada por um buffer de 4 números da seguinte maneira:

```
M = a b
    c d

buf: a b c d
```

Crie uma palavra `get (addr i j -- a)` que lê um endereço `addr` da pilha, que
aponta para o início do buffer, e dois índices `i` e `j` para linhas e colunas,
respectivamente, e deixa o número correspondente da matriz no topo da pilha. Por
exemplo, `buf 0 1 get` deve deixar `b` no topo da pilha.

Depois cria a palavra `M@ (addr -- )` que imprime uma matriz 2x2 formatada a
partir do buffer. Por exemplo, `buf M@` deve imprimir:

```a b
c d
```
