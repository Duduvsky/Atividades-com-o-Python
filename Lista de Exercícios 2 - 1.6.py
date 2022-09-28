#6. Escreva um programa que lê um valor n inteiro e positivo e que calcula a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.

n = int(input(" Insira um valor inteiro e positivo: "));
s = 1

for cont in range (2,n+1):
    s = s + ( 1/cont )
    
print(s)