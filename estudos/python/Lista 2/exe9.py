lado_a = int(input("Digite o lado A: "));
lado_b = int(input("Digite o lado B: "));
lado_c = int(input("Digite o lado C: "));

soma1 = lado_a + lado_b;
soma2 = lado_b + lado_c;
soma3 = lado_a + lado_c;

if (soma1 > lado_c and soma2 > lado_a and soma3 > lado_b):
    if (lado_a == lado_b and lado_b == lado_c):
        print("É um triângulo equilátero.");
    elif (lado_a == lado_b or lado_a == lado_c or lado_b == lado_c):
        print("É um triângulo isósceles");
    else:
        print("É um triângulo escaleno.");
else:
    print("Não formam um triângulo");

