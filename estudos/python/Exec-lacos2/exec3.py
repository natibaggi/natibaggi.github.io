letra = input("Digite uma letra: ");
quantidade = 1;

while True:
    letraAnterior = letra
    letra = input("Digite uma letra: ");

    if letra >= letraAnterior:
        quantidade = quantidade + 1;

    else:
        break

print(quantidade)
