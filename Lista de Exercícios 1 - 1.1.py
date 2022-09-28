# 1.	Elabore um programa em Python que leia a medida de um raio de um círculo e efetue o cálculo da sua área, exibindo o resultado ao final.
#  (dica: use math.pi()  )
import math

raio = float(input("Informe o raio para que seja feito o cálculo da área: "))

pot = raio ** 2
area = math.pi * pot

print("A área será: %.2f" %(area))