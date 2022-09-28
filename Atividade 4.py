#Atividade 4 - Estrutura Condicional – Quadrante 

x = float(input("\n Informe a coordenada x : "));
y = float(input("\n Informe a coordenada y : "));

if x == 0 and y == 0:
    print("\n Origem ");
elif x == 0 and y > 0:
    print("\n **Se encontra no Eixo Y**");
elif x > 0 and y == 0:
    print("\n **Se encontra no Eixo X**");
elif x > 0 and y > 0:
    print("\n Eixo x = %.2f \n Eixo y = %.2f \n **Se encontra no quadrante 1**" %(x, y));
elif x < 0 and y > 0:
    print("\n Eixo x = %.2f \n Eixo y = %.2f \n **Se encontra no quadrante 2**" %(x, y));
elif x < 0 and y < 0:
    print("\n Eixo x = %.2f \n Eixo y = %.2f \n **Se encontra no quadrante 3**" %(x, y));
else:
    print("\n Eixo x = %.2f \n Eixo y = %.2f \n **Se encontra no quadrante 4**" %(x, y));