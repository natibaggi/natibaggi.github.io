numero = input("Digite um número: ");

tamanho = len(numero)
print (tamanho);

inverso = "";
posicao = 0;

while posicao <= tamanho:
    inverso = inverso + (numero[tamanho - 1]);
    
    posicao = posicao + 1;
    tamanho = tamanho - 1;

print(inverso)
