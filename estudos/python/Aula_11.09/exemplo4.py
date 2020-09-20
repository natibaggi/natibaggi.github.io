preco = float(input("Digite o preço do produto: "));
quantidade = int(input("Digite a quantidade do produto: "));

valor_compra = preco * quantidade;
desconto = 0.05;

print("Total da compra: R$", valor_compra);

if valor_compra > 200:
    opcao_pagamento = int(input("Digite 1 para desconto a vista e 2 para valor parcelado: "));
    
    if opcao_pagamento == 1:
        valor_desconto = valor_compra * desconto;
        print("Valor do desconto: R$ %.2f" % valor_desconto);
        
        valor_final = valor_compra - valor_desconto
        print("Valor total da compra: R$ %.2f " % valor_final);
    elif opcao_pagamento == 2:
        quant_parcelas = int(input("Digite o número de parcelas (De 1 a 10): "));

        if quant_parcelas >= 1 and quant_parcelas <= 10:
            valor_parcelado = valor_compra / quant_parcelas;
            print("Valor da parcela: R$ %.2f " % valor_parcelado);
        else:
            print("Opção inválida!");

    else:
        print("Opção inválida!");