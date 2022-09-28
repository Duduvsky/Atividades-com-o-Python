#Dada uma sequência de números inteiros informada pelo usuário, calcular e imprimir os seus quadrados (Melhorando o código)

from re import S


resp = input('Deseja informar um valor para o cálculo do quadrado (s - sim ou n - não)?')

while resp == 's' or resp == 'S':
    num = int (input('Digite um número: '))
    quad = num * num
    
    print('O quadrado de %d = %d' %(num, quad))
    
    resp = input('Deseja informar um valor para o cálculo do quadrado (s - sim ou n - não)?')

print("** Fim do programa ! **")