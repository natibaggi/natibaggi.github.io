num1 = int(input("Digite o 1o número: "));
num2 = int(input("Digite o 2o número: "));
operador = input("Digite o operador desejado: ");

if operador == "+":
    resultado = num1 + num2;
elif operador == "-":
    resultado = num1 - num2;
elif operador == "*":
    resultado = num1 * num2;
elif operador == "/":
    resultado = num1 / num2;

print("O resultado é: %d." % resultado);