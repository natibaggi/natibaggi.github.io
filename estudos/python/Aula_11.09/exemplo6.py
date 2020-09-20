a = int(input("Digite o 1o numero: "));
b = int(input("Digite o 2o numero: "));
x = int(input("Digite o 3o numero: "));

if x >= a and x <= b:
    print("está")
    if x - a < b - x:
        print("x, está mais proximo de", a)

else:
    print("Não está no intervalo")