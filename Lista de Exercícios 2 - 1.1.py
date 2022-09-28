#1.	Faça um programa para ler dois inteiros e imprimir o resultado do quadrado da diferença do primeiro valor pelo segundo.

n1 = int(input(" Insira o primeiro número inteiro"));
n2 = int(input(" Insira o segundo número inteiro"));

dif = n1 - n2
resul = dif ** 2

print(" A diferença ao quadrado de %d e %d é = %d" %(n1, n2, resul));
