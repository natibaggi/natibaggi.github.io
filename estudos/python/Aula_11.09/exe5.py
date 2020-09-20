caracter = input("Insira um caracter: ")

if "0" <= caracter <= "9" :
    numero = int(caracter);
    if (numero % 2) == 0:
        print ("É um digito par.");
    else:
        print ("É um digito impar.");
else:
    letra = caracter.upper();
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
         print ("É uma vogal.");
    else:
        print ("É uma consoante.")