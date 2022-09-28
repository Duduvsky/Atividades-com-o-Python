#Faça um programa, utilizando a estrutura while, que permita o usuário fazer contas de adição entre dois valores enquanto ele desejar.

resp = input(" Deseja informar um valor para o cálculo de adição entre dois valores ( s = Sim ou n = Não )?")

while resp == 's' or resp =='S':
    num1 = float(input(" Informe o primeiro número para a adição: "))
    num2 = float(input(" Informe o segundo número para a adição: "))
    soma = num1 + num2
    print("A adição do %d + %d = %d" %(num1, num2, soma))
    resp = input(" Deseja informar um valor para o cálculo de adição entre dois valores ( s = Sim ou n = Não )?")

print(" Fim do programa")