#5.	Elabore um programa que calcule e imprima o valor de xn. 
# O valor de n deverá ser maior do que 1 e inteiro e o valor de x deverá ser maior ou igual a 2 e inteiro. 
# O cálculo da potência deve ser feito sem o uso de funções da biblioteca de math.

x = int(input("Insira um número maior que 2 e ele deve ser inteiro: "))
n = int(input("Insira um número maior que 1 e ele deve ser inteiro: "))

xn = x ** n

print(" O cálculo de %d elevado a %d é = %d" %(x, n, xn))