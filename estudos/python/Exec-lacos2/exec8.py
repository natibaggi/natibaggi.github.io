n = int(input("Digite um número: "));

binario = 0;
contador = 1;

while n >= 1:    
    resto = n % 2;

    soma = resto * contador;
    binario = binario + soma;
    contador = contador * 10;

    n = n // 2;

print(binario)
