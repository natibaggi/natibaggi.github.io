executar = input("Você quer calcular? Sim(S) ou Não(N)");

while executar == "S":
    num1 = int(input("Digite o 1o número: "));
    num2 = int(input("Digite o 2o número: "));
    operador = input("Digite o operador: ");

    if operador == "+":
        resultado = num1 + num2;
    elif operador == "-":
        resultado = num1 - num2;
    elif operador == "*":
        resultado = num1 * num2;
    elif operador == "/":
        if num2 == 0:        
            print("Divisão por zero!");
            executar = input("Você quer calcular? Sim(S) ou Não(N)");
            continue
        else:
            resultado = num1 / num2;
    
    print("%d %c %d = %d\n" % (num1, operador, num2, resultado));
    executar = input("Você quer calcular? Sim(S) ou Não(N)");
