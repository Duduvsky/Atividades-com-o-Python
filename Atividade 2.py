#Atividade 2 - Condicional Bhaskara

a = float(input("\n Informe o valor de a : "));
b = float(input("\n Informe o valor de b: "));
c = float(input("\n Informe o valor de c: "));

delta = ( b ** 2) - 4 * a * c

if a == 0:
    print("\n Impossível calcular !");
elif delta < 0:
    print("\n Impossível de calcular !");
else: 
    r1 = (-b + delta ** (1/2)) / (2 * a)
    r2 = (-b - delta ** (1/2)) / (2 * a) 

    print("\n r1:= %.5f \n r2 = %.5f" %(r1, r2));
    