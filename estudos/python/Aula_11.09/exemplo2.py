preco = float(input("Digite o preço do produto: "));
quantidade = int(input("Digite a quantidade do produto: "));

valor_compra = preco * quantidade;
desconto = 0.05;
parcelamento = 4;

print("Total da compra: R$", valor_compra);

if valor_compra > 200:
    opcao_pagamento = int(input("Digite 1 para desconto a vista e 2 para valor parcelado em 4 vezes: "));
    
    if opcao_pagamento == 1:
        valor_desconto = valor_compra * desconto;
        print("Valor do desconto: R$ %.2f" % valor_desconto);
        
        valor_final = valor_compra - valor_desconto
        print("Valor total da compra: R$ %.2f " % valor_final);
    elif opcao_pagamento == 2:
        valor_parcelado = valor_compra / parcelamento;
        print("Valor da parcela: R$ %.2f " % valor_parcelado);
    else:
        print("Opção inválida!");
