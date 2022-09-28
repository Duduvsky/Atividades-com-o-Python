#Escrever um programa que lê 10 valores inteiros para a variável “a”, um de cada vez, 
# e conta quantos destes valores são negativos, exibindo esta informação na tela.
contp=0
contn=0
lista = [ ]
for cont in range(1,11):
    lista.append(float(input("Insira 10 números:")));
print(lista)
for a in lista :
    if a > 0:
        contp= contp + 1
    else:
        contn= contn + 1
        

print("Quantidade de números negativos é: %d " %(contn)) 


    
    
        