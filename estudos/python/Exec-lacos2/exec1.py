n = int(input("Digite um número: "));
multiplica = 0;

for i in range(1,n):
    multiplica = i * (i + 1) * (i + 2)

    if multiplica == n:
        print("O número é triangular");
        break

if multiplica != n:
    print("O número não é triangular");