#6 - Elaborar um programa que solicita a entrada de 3 valores (a, b, c) 
# e verifica se esses valores podem formar ou não um triângulo. 
# Você deve considerar que os valores lidos são inteiros e positivos. 
# Caso os valores formem um triângulo, exiba essa informação e o valor do perímetro deste triângulo. 
# Se não formarem triângulo, apenas exiba uma mensagem com essa informação. 
# (Obs.: Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.)

a = float(input(" Informe um número inteiro e positivo: "))
b = float(input(" Informe um número inteiro e positivo: "))
c = float(input(" Informe um número inteiro e positivo: "))

if a > ( b + c ) :
    print("Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados !")
elif b > ( a + c ) :
    print("Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados !")
elif c > ( a + b ) :
    print("Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados !")
else:
    peri = a + b + c
    print(" Estes valores pode formar um triângulo ! \n Sendo seu perímetro = %.1f" %(peri))
