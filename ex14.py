#Faça um programa que leia 15 números inteiros, calcule e exiba a média dos números pares.

i = 1;
soma = 0
qtde = 0
while i <=15:      # Le os 15 numeros
    num = int (input('Informe um número: '))
    if num % 2 == 0:   # verifica se é par
        soma = soma + num
        qtde+=1
    i+=1
if (qtde > 0):     # Calcula media
    media = soma / qtde
    print('Média: %.1f' %(media))
else:
    print('Não houve números pares.')
