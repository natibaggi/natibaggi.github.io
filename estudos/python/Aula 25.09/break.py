numero = int(input("Digite um número: "));

divisor = 2;

while divisor <= numero:
    if numero % divisor == 0:
        break

    divisor += 1

if divisor == numero:
    print("O número é primo");
else:
    print("O número não é primo");