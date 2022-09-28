#Atividade 3 - Estrutura Condicional – Intervalo

num = float(input("\n Informe um número: "));

if num >= 0 and num <= 25:
    print("\n O %.2f pertende a faixa de [0, 25]" %(num));
elif num > 25 and num <= 50:
    print("\n O %.2f pertende a faixa de [25, 50]" %(num));
elif num > 50 and num <= 75:
    print("\n O %.2f pertende a faixa de [50, 75]" %(num));
elif num > 75 and num <=100:
    print("\n O %.2f pertende a faixa de [75, 100]" %(num));
else:
    print("\n Este número está fora do intervalo");
    
    