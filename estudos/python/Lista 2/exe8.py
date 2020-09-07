lado_a = int(input("Digite o lado A: "));
lado_b = int(input("Digite o lado B: "));
lado_c = int(input("Digite o lado C: "));

soma1 = lado_a + lado_b;
soma2 = lado_b + lado_c;
soma3 = lado_a + lado_c;

if (soma1 > lado_c and soma2 > lado_a and soma3 > lado_b):
    print("Formam um triângulo");
else:
    print("Não formam um triângulo");

