#4.	Uma agência de uma cidade do interior tem, no máximo, 10.000 clientes. Faça um programa que leia o número da conta e o saldo de cada cliente. 
# A leitura de clientes termina quando for digitado -999 para número da conta ou quando atingir 10.000 clientes. 
# O programa deve calcular e imprimir o total de clientes com saldo negativo, o total de clientes da agência e o saldo da agência.

saldo = 0
nneg = 0
saldob = 0
cliente = 0

while saldo != 999 and conta != 10000:
    saldo = int(input("Insira o saldo da sua conta: "));
    conta = int(input("Informe sua conta entre -999 a 10.000 : "))
    
    cliente = cliente + 1
    saldob = saldob + saldo
    
    if saldo < 0:
        nneg = nneg + 1

print(" O número de clientes com saldo negativo é: %d" %(nneg));
print(" O total de clientes da agência é: %d" %(cliente));
print(" O saldo do banco de todos os %d clientes é = R$ %.2f" %(cliente, saldob));
