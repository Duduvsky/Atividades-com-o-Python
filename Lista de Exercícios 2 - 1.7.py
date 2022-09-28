#7. Seja a seguinte série: 1, 4, 9, 16, 25, 36, ... Escreva um programa que gere esta série até o N-ésimo termo, digitado pelo usuário.

x = int(input(" Insira um número: "));
var = 3
n = 1
for cont in range (1,x+1):
    print(n)
    n = n + var
    var = var + 2