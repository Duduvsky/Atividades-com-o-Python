#2.	Escreva um programa que calcule o valor da hipotenusa de um triangulo retângulo, dado o valor de cada um dos catetos.

b = int(input("Insira o primeiro cateto: "))
c = int(input("Insira o segundo cateto: "))

hipo = b**2 + c**2
a = hipo ** (1/2)

print("A hipotenusa dos valores %d e %d é = %d" %(b, c , a))