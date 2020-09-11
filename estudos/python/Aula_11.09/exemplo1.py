num1 = int(input("Digite o numero 1: "));
num2 = int(input("Digite o numero 2: "));

if num1 == num2:
    print("Eles são iguais,", end = " ");
    if num1 % 2 == 0:
        print("e são pares.");
    else:
        print("e são impares.")

else:
    print("Eles são diferentes.");