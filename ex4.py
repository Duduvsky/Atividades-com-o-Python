#Faça um programa que faça a leitura de 10 valores inteiros e, para cada valor, o programa deve informar se o número é par ou ímpar.
for cont in range(1,11):
    if cont % 2 == 0:
        print("%1d é par!" %(cont));
    else:
        print("%1d é impár!" %(cont));
