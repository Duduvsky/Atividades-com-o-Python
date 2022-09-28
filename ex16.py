#Dada uma sequência de números inteiros informada pelo usuário, calcular e imprimir os seus quadrados

num = int (input('Digite um número – 0 (zero) para sair.'))

while num != 0:
    quad = num * num
    print('O quadrado de %d = %d' %(num, quad))
    num = int (input('Digite um número – 0 (zero) para sair.'))

print("** Fim do programa ! **")