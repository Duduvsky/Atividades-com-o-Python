fem = 0
mas = 0
nide = 0
quantMas = 0
idatot = 0
soma = 0

for cont in range(1,11):
    idade = float(input(" Insira a sua idade:"));
    sexo = int(input("** Genero **\n 1 - Mulher\n 2 - Homem\n 3 - Outros \n"));

    if  ( idade > 21 )  and  sexo == 2 :
        quantMas = quantMas + 1
        soma = soma + idade
    if idade > 21:
        idatot = idatot + 1
    if sexo == 1:
        fem = fem + 1
    elif sexo == 2:
        mas = mas + 1
    else:
        nide = nide + 1
    
     
media = soma / quantMas

print("\n ** Quantidade de Generos ** \n Mulheres : %d \n Homens : %d \n Outros : %d " %(fem, mas, nide));
print("\n Alunos com mais de 21 anos : %d " %(idatot));
print("A médio de idade dos alunos Masculino acima de 21 anos é : %d" %(media));


