# numero = int(input("Digite um número: "));
# quantidade = 0;

# for contador in range(2, numero + 1):
#     if numero % contador == 0:
#         quantidade = quantidade + 1;

# if quantidade == 1:
#     print("O numero é primo");
# else:
#     print("O numero NAO é primo");
        

primeiro = int(input("Digite o primeiro número: "));
ultimo = int(input("Digite o último número: "));

for intervalo in range(primeiro, ultimo + 1):
    quantidade = 0;

    for contador in range(2, intervalo + 1):
        if intervalo % contador == 0:
            quantidade = quantidade + 1;
    
    if quantidade == 1:
        print(intervalo, end= " ");