dia1 = int(input("Coloque o 1o dia: "));
mes1 = int(input("Coloque o 1o mês: "));
ano1 = int(input("Coloque o 1o ano: "));

dia2 = int(input("Coloque o 2o dia: "));
mes2 = int(input("Coloque o 2o mês: "));
ano2 = int(input("Coloque o 2o ano: "));

data1 = str(dia1) + "/" + str(mes1) + "/" + str(ano1)
data2 = str(dia2) + "/" + str(mes2) + "/" + str(ano2)

if (ano1 < ano2):
    print ("Essa data ocorre primeiro: ", data1);
    
elif (ano2 < ano1):
    print ("Essa data ocorre primeiro: ", data2);
    
elif (ano1 == ano2):
    if (mes1 < mes2):
        print ("Essa data ocorre primeiro: ", data1);
    elif (mes2 < mes1):
        print ("Essa data ocorre primeiro: ", data2);

    elif (mes1 == mes2):
        if (dia1 < dia2):
            print ("Essa data ocorre primeiro: ", data1);
        elif (dia2 < dia1):
            print ("Essa data ocorre primeiro: ", data2);
        elif (dia1 == dia2):
            print("As datas são iguais.");







