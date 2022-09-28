# Em uma turma do curso de ADS, o coordenador do curso fez uma rápida pesquisa com os alunos para levantar alguns dados. 
# Você deve fazer um programa que solicite ao usuário que informe a idade dele e o gênero que ele se identifica (F, M ou Não identificado (N)) 
# e calcule e exiba:
#- A quantidade de alunos em cada gênero;
#- A quantidade de alunos com mais de 21 anos;
#- A média das idades dos alunos que se identificam com o gênero masculino. 

masc = 0
fem = 0
semg = 0
quantmasc = 0
idadesoma = 0
alunoquant = 0

resp = input(" Deseja continuar a pesquisa ( s = Sim ou n = Não )?")
# Primeira pergunta para o usuário

while resp == 's' or resp =='S':
    idade = float(input("Informe a idade: "));
    sexo = float(input("** Genero ** \n 1 - Mulher\n 2 - Homem\n 3 - Outros \n"));
    # Pergunta as informações para o usuário

    if idade > 21 and sexo == 2:
        quantmasc += 1      # Ter a quantidade dos alunos Homens maiores de 21 anos
        idadesoma = idadesoma + idade   # Ter a soma das idades desses alunos
    if idade > 21:
        alunoquant += 1     # Ter a quantidade geral dos alunos maiores de 21 anos
    if sexo == 1:   
        fem += 1            # Ter a quantidade dos alunos que são Mulheres
    elif sexo == 2:
        masc += 1           # Ter a quantidade dos alunos que são Homens
    else:
        semg += 1           # Ter a quantidade dos alunos que não se identificam como Homem ou Mulher
    resp = input(" Deseja continuar a pesquisa ( s = Sim ou n = Não )?")
    # Pergunta se o Usuário gostaria de continuar a introduzir informações

mediaidademasc = idadesoma / quantmasc      # Calcular a média das idades dos homens

print("\n ** Quantidade de Generos ** \n Mulheres : %d \n Homens : %d \n Outros : %d " %(fem, masc, semg));
print("Alunos com mais de 21 anos : %d " %(alunoquant));
print("A médio de idade dos alunos Masculino acima de 21 anos é : %d" %(mediaidademasc));