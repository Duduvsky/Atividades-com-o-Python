#Calcula a média de 6 alunos.
for cont in range(1,7):
    print('\n*** Aluno %d ***' %cont)
    n1=float(input("informe a primeira nota:"))
    n2=float(input("Informe a segunda nota:"))
    media= (n1+n2)/2
    print("Media das notas %.1f e %.1f = %.1f" %(n1,n2, media))
