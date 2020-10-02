numero = int(input("Digite um número: "));

menor = numero

while numero != -99:
    numero = int(input("Digite um número: "));

    if numero < menor and numero != -99:
        menor = numero

print("O menor número é:", menor);
