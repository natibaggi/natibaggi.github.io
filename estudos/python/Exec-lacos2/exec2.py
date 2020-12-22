numero = int(input("Digite um número: "));
sequencia = 0;

for contador in range(1, numero + 1):
    sequencia = sequencia + contador;
    print(sequencia, end= " ");