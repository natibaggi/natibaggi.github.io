n = int(input("Digite a quantidade de números: "));

numero = int(input("Digite um número inteiro: "));
menor = numero;


for i in range(1,n):
    numero = int(input("Digite um número inteiro: "));

    if numero < menor:
        menor = numero;

print("O menor número é:", menor);
