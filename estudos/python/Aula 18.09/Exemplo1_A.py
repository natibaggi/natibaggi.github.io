num1 = float(input("Digite o 1o número: "));
num2 = float(input("Digite o 2o número: "));

resposta = 0;

while num1 >= num2:
    num1 = num1 - num2;

print ("O resto é", num1)
