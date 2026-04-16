# Questão 08

Implemente as seguintes palavras em Forth. Você pode usar as funções de
manipulação da pilha, funções numéricas e estruturas de controle de fluxo que
foram apresentadas em aulas anteriores. Você também pode criar palavras
auxiliares para ajudar a resolver os exercícios, mas não pode usar variáveis ou
arrays. 

Antes de enviar, certifique-se de que o código contenha apenas definições de
palavras, sem nenhum código de teste ou execução posterior.


## `sign'`

Crie uma palavra `sign' ( n -- s )` que lê o topo da pilha e deixa o seguinte
valor:
- `-1` se o número for negativo
- `0` se o número for zero
- `1` se o número for positivo

Você não pode usar a palavra `sign` do Forth.

## `sum`

Crie uma palavra `sum ( ... n -- soma )`. `n sum` lê os `n` números do topo da
pilha e deixa a soma deles no topo.

## `has-zero`

Crie uma palavra `has-zero ( ... -- ... flag )` que lê todos os números da pilha
e deixa uma flag indicando se algum dos números é zero. Importante: a pilha deve
ser preservada na execução.

---

## Dicas e funções úteis

### Funções de manipulação da pilha
- `dup` duplica o número do topo da pilha, ou seja, `a` se torna `a a`.
- `pick` copia um número da pilha para o topo, onde `n pick` copia o número que 
  está `n` posições abaixo do topo. Por exemplo, `0 pick` equivale a `dup`, 
  `1 pick` equivale a `over`.
- `swap` troca os dois números do topo da pilha, ou seja, `a b` se torna `b a`.
- `over` copia o segundo número do topo da pilha para o topo, ou seja, `a b` se torna `a b a`. 
- `rot` move o terceiro número do topo da pilha para o topo, ou seja, `a b c` se torna `b c a`.
- `-rot` move o topo da pilha para o terceiro número, ou seja, `a b c` se torna `c a b`.
- `2dup` duplica os dois números do topo da pilha, ou seja, `a b` se torna `a b a b`.

### Funções numéricas
- `max / min` deixam o maior / menor dos dois números do topo da pilha, ou seja, `a b max` deixa o maior entre `a` e `b` no topo da pilha.

### Controle de fluxo/ambiente/execução
- `depth` deixa o número de itens na pilha, ou seja, `a b c depth` deixa `3` no topo da pilha.
- `exit` termina a execução da palavra atual, retornando o controle para a palavra que a chamou.
- `if ... else ... then` é uma estrutura de controle condicional.
- `begin ... until` loop estilo do-while.
- `begin ... while ... repeat` loop estilo while.
- `do ... loop` loop estilo for.
- `?do ... loop` igual ao anterior, mas pula a execução se o limite inferior for igual ao limite superior.
