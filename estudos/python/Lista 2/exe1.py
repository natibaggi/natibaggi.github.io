preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))
desconto = 0.9
calculo = preco_unitario * quantidade * desconto

print("A resposta é: " + str(calculo))