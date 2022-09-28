#Faça um programa que imprima a tabuada de um numero “n” (dado de entrada do seu programa)  utilizando estrutura de repetição.
n1=float(input("Insira um número inteiro:"))
for cont  in range(1, 11):
    print('\n*** Tabuada do %d ***' %n1)
    tabu= cont * n1
    print(" %d x %d = %d" %(n1, cont, tabu))
    
