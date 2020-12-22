entrada = float(input("Digite um número: "));

soma = 0;
quantidade = 0;

while (entrada != 0):
    soma = soma + entrada;
    quantidade = quantidade + 1;

    entrada = float(input("Digite um número: "));

media = soma / quantidade;

print("A média dos valores é:", media);