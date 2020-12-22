i = int(input("Digite o 1o número: "));
j = int(input("Digite o 2o número: "));
n = int(input("Digite a quantidade de números: "));

limite = 0;

for contador in range(1, n + 1):
    if limite >= n:
        break;
        
    if (i * contador) < (j * contador):
        print(i * contador, end=" ");
        print(j*contador, end= " ");
        limite = limite + 2;
    elif (i * contador) > (j * contador):
        print(j*contador, end= " ");
        print(i * contador, end=" ");
        limite = limite + 2;
    