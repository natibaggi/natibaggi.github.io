n = int(input("Digite um número: "));

quadrado = 0;
menor_num_quadrado = 0;

for i in range(0, n):
    quadrado = i*i;
    if quadrado <= n:
        menor_num_quadrado = i;
    else:
        break;

print(menor_num_quadrado)
