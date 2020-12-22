# Crie um programa para um site de compras que solicita o crédito do cliente
# e verifica, a cada item comprado, se há crédito suficiente para incluir 
# o item no carrinho. A compra de cada cliente deve ser finalizada quando 
# for inserido um item com valor zero.

while True:
    novaCompra = input("Inserir nova compra? (S ou N)")
    if novaCompra == "N":
        break
    
    credito = float(input("Digite o crédito do cliente: "));
    valorItem = float(input("Digite o valor do item comprado: "));
    valorCompra = 0;

    while valorItem != 0:
        if valorItem <= credito:
            credito = credito - valorItem;
            valorCompra = valorCompra + valorItem;
        else:
            print("Você não tem saldo");

        valorItem = float(input("Digite o valor do item comprado: "));

    print("O valor da compra foi de:", valorCompra);