\ Responda os exercícios aqui. Lembre-se de remover qualquer código fora de
\ definições antes de enviar a resposta final.

\ ==============================================================================
\ DEFINIÇÕES
\ ==============================================================================

: sign' ( n -- s )
  dup 0 > if drop 1 exit then
  0 < if -1 else 0 then ;

: sum ( ... n -- soma )
  0 swap
  ?do + loop ;

: has-zero ( ... -- ... flag )
  depth 0 swap
  ?do
    i 1+ pick 0= if drop -1 leave then
  loop ;

\ ==============================================================================
\ TESTE
\ ==============================================================================
\ Não esqueça de apagar ou comentar código fora das definições antes de enviar 
\ a submissão final ou rodar os testes usando o pytest.

42 sign' . cr \ deve imprimir "1"
-42 sign' . cr \ deve imprimir "-1"
0 sign' . cr \ deve imprimir "0"

-1 1 2 3 3 sum .s cr \ deve imprimir "-1 6"
clearstack

-1 -1 0 1 2 sum .s cr \ deve imprimir "-1 -1 1"
clearstack

0 1 2 3 has-zero .s cr \ deve imprimir "0 1 2 3 -1" (true)
clearstack

1 2 3 has-zero .s cr \ deve imprimir "1 2 3 0" (false)
clearstack

bye