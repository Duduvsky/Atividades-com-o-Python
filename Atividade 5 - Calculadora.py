
resp = input(" Deseja usar a calculadora ( s = Sim ou n = Não )?")

while resp == 's' or resp == 'S':
    resp = float(input("** Informe qual operação deseja realizar ** \n 1 - Adição entre 2 números \n 2 - Diferença entre dois números \n 3 - Produto entre 2 números \n 4 - Divisão entre 2 números \n 5 - Para sair \n Informe o número: "))
    num1 = float(input(" Informe o primeiro numero: "))
    num2 = float(input(" Informe o segundo número: "))
    
    if resp == 1 :
        soma = num1 + num2
        print("A soma dos números %.1f e %.1f é = %.1f" %(num1, num2, soma))
    elif resp == 2 and num1 > num2 :
        sub1 = num1 - num2
        print("A diferença entres os números %.1f e %.1f é = %.1f" %(num1, num2, sub1))
    elif resp == 2 and num1 < num2 :
        sub2 = num2 - num1
        print(" A diferença entres os números %.1f e %.1f é = %.1f" %(num2, num1, sub2))
    elif resp == 3 :
        mult = num1 * num2
        print("O produto dos números %.1f e %.1f é = %.1f" %(num1, num2, mult))
    elif resp == 4 and num1 == 0 and num1 < num2 :
        print("Não é possível fazer divisão por zero")
    elif resp == 4 and num2 == 0 and num1 > num2 :
        print("Não é possível fazer divisão por zero")
    elif resp == 4 and num1 > num2 :
        div = num1 / num2
        print("A divisão entre os números %.1f e %.1f é = %.1f " %(num1, num2, div))
    elif resp == 4 and num1 < num2 :
        div1 = num2 / num1
        print("A divisão entre os números %.1f e %.1f é = %.1f " %(num2, num1, div1))
    else:
        print("** ERRO ** Operação Inválida ** ERRO **")
    
    resp = input(" Deseja continuar usar a calculadora ( s = Sim ou n = Não )?")

print("Calculadora fechada !")
