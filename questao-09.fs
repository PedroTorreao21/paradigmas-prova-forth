\ Responda os exercícios aqui. Lembre-se de remover qualquer código fora de
\ definições antes de enviar a resposta final.

\ ==============================================================================
\ DEFINIÇÕES
\ ==============================================================================

: get ( addr i j -- x ) ;
: M@ ( addr -- ) ;


\ ==============================================================================
\ TESTES
\ ==============================================================================
\ Não esqueça de apagar ou comentar código fora das definições antes de enviar 
\ a submissão final ou rodar os testes usando o pytest.

create m1 1 , 2 , 3 , 4 ,
create m2 5 , 6 , 7 , 8 ,

m1 M@ cr
m2 M@ cr

m1 0 0 get . cr \ deve imprimir "1"
m1 0 1 get . cr \ deve imprimir "2"
m1 1 0 get . cr \ deve imprimir "3"
m1 1 1 get . cr \ deve imprimir "4"

bye
