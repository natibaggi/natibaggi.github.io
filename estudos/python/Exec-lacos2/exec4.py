numero = int(input("Digite um número: "));

while True:
    ultimo = numero % 10;    
    
    numero = numero // 10;

    penultimo = numero % 10;

    if ultimo % 2 == 0 and penultimo % 2 == 1:
        print("é");
        break
    elif ultimo % 2 == 1 and penultimo % 2 == 0:
        print("é");
        break
    else:
        print("Não é");
        break