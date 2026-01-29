'''
IF-ELSE é uma estrutura condicional para tomada de decisões
 
OPERADORES RELACIONAIS
 
IGUAL
== (1 == 1 TRUE) | (2 == 1 FALSE)
 
DIFERENTE
!= (1 != 1 FALSE) | (2 != 1 TRUE)
 
MENOR QUE
< (1 < 1 FALSE) | (2 < 1 FALSE)
 
MAIOR QUE
> (1 > 1 FALSE) | (2 > 1 TRUE)
 
MENOR OU IGUAL
<= (1 <= 1 TRUE) | (2 <= 1 FALSE)
 
MAIOR OU IGUAL
>= (1 >= 1 TRUE) | (2 >= 1 TRUE)
 
OPERADORES LÓGICOS
 
and (E) (1 == 1 and 2 == 1 FALSE)
 
or (OU) (1 == 1 or 2 == 1 TRUE)
'''

produto = input('Digite um produto:')
quantidade = int(input('Digite a quantidade: '))


if quantidade > 0:
    print("Produto possui estoque")
else:
    print("Produto NÂO POSSUI estoque")
