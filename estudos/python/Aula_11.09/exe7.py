num1 = float(input("Digite o 1o número: "));
num2 = float(input("Digite o 2o número: "));

if num1 < num2:
    print("O numero %.2f é menor que %.2f." % (num1, num2));

elif num2 < num1:
    print("O numero %.2f é menor que %.2f." % (num2, num1));

else:
    print("Os dois numeros são iguais.")