#Calcula média de 30 alunos
for cont in range(1,31):
    n1=float(input("Informe a primeira nota:"))
    n2=float(input("Infome a segunda nota:"))
    media= (n1+n2)/2
    print("Media das notas do %d aluno %.1f e %.1f = %.1f" %(cont, n1, n2, media))