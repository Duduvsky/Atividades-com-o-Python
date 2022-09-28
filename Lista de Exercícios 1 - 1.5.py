conveniado = 100
plano1 = 60
plano2 = 90
plano3 = 130
plano4 = 250
plano5 = 400
valortotal = 0

idade = int(input("Informe sua idade para a realização do cálculo com o adicional: "))

if idade <= 10 :
    valortotal = conveniado + plano1
elif idade > 10 and idade <= 30:
    valortotal = conveniado + plano2
elif idade > 30 and idade <= 45:
    valortotal = conveniado + plano3
elif idade > 45 and idade <= 59:
    valortotal = conveniado + plano4
else:
    valortotal = conveniado + plano5

print(" Por sua idade ser %d \n O valor a ser pago será %d" %(idade, valortotal))
