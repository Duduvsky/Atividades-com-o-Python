#3. Faça um programa que leia a média de alunos de uma determinada turma, encontre e exiba o maior valor de média inserida. 
# Obs.: Não há informação prévia sobre a quantidade de alunos da turma

resp = str(input("** Para começar o programa, responda ** \n s - Sim\n n - Não\n: "));
alunot = 0
maiorm = 0

while resp == 's' or resp =='S':
    media = float(input("Insira a média do aluno: "))
    alunot = alunot + 1
    
    if media > maiorm:
        maiorm = media
    
    resp = input("** Responda ** \n s - Sim\n n - Não\n** Para continuar o programa **\n: ");

print(" A maior média de um total de %d de alunos é: %d" %(alunot, maiorm))