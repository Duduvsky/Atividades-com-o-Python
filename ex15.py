soma = 0
qtde = 0

# le 1a idade idade
idade = int (input('Informe uma idade – digite um valor <0 para finalizar: : '))

while idade >=0:
    if idade % 2 == 0:   # verifica se é par
        soma = soma + idade
        qtde+=1
    
    # le proxima idade
    idade = int (input('Informe uma idade – digite um valor <0 para finalizar: : '))

if (qtde > 0):     # Calcula media
    media = soma / qtde
    print('Média: %.1f' %(media))
else:
    print('Não houve números pares.')