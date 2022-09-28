#Faça um programa que leia 10 valores inteiros, um de cada vez, 
# e encontre quantos destes valores são pares, quantos são ímpares, 
# além de calcular a média de todos os números informados. 
# Todos os dados calculados devem ser exibidos ao final do programa

numPar = 0
numImp = 0
soma = 0
for cont in range(1,11):
    a = float(input("Insira um número aqui:"));
    if a % 2 == 0 :
        numPar= numPar + 1;
    else:
        numImp = numImp + 1;
    soma= soma + a

media = soma / 10;

print("Quantidade de número pares: %d" %(numPar));
print("Quantidade de números impares: %d" %(numImp));
print("A média desses valores vai ser: %.1f" %(media));

