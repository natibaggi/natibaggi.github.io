# a = int(input('a: '))
# b = int(input('b: '))

# m = 0;

# while b > 0:
#     m = m + a
#     b = b - 1

# print("a * b =", m)





# n = int(input('n: '))
# d = n % 10

# while True:
#     n = n // 10

#     if  n <= 9:
#         break

# if d == n:
#     print("Iguais")
# else: 
#     print("Diferentes")





# n = int(input('n: '))
# s = 0;

# for i in range(1, n):
#     if n % i == 0:
#         s += i;

# if n == s: print('perfeito')
# else: print('não perfeito')





# x = int(input("Digite um numero: "))
# b = x % 2
# if b == 0:
#     print('par')
# else:
#     print('impar')




n = int(input("n: "));

for contador in range(n, 0, -1):
    print(contador, end= " ");
