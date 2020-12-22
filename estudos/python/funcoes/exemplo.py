# def quociente(a,b):
#     soma = cont = 0

#     while soma < (a - 1) and a > b:
#         soma = soma + b
#         cont = cont + 1

#     print(cont)

# a = 5
# b = 10

# quociente(a,b)




# def misterio(a, b, c):
#     d = False
#     e = 0
#     f = 0
#     g = c-1

#     while (f<=g) and (not d):
#         h = (f+g) // 2
#         e += 1
        
#         if a == b[h]:
#             d = True
#         elif a < b[h]:
#             g = h - 1
#         else:
#             f = h + 1
        
#         print(g)


#     return e

# a = 10
# b = [2,4,6,7,10,15,17,20]
# c = 8

# misterio(a,b,c)




def vogais(v, n):

    for i in range(0, n):

        if v[i] == "a" or v[i] == "e" or v[i] == "i" or v[i] == "o" or v[i] == "u":
            print(v[i],end= " ")


v = ["i", "!", "a", "3", "E"]

vogais(v, 5)