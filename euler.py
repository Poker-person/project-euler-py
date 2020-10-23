# https://projecteuler.net/problem=2

# 1 - enconte a soma de todos os numeros naturais multiplos de 3 ou 5 ate 1000
#multiplos = []

#for i in range(1, 1000):
#    if (i % 3 == 0) or (i % 5 == 0):
#        multiplos.append(i)

#print(sum(multiplos))

# 2 - Encontre a soma dos numeros pares da sequencia de Fibonacci ate 4 milhoes
#x1 = 0
#x2 = 0
#fibonacci_par = []

#for i in range(1, 40000):
#    x2 = x2 + x1
#    x1 = x2 - x1
#    if x2 == 0:
#        x2 = x2 + 1
#    if x1 % 2 == 0:
#        fibonacci_par.append(x1)

#print(sum(fibonacci_par))

# 3 - What is the largest prime factor of the number 600851475143?
#cu = []
#res = []

#for num in range(1, 600851475143):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            if (600851475143 % num) == 0:
#                res.append(num)

#print("O maior fator primo de 600851475143 é", res[-1])

# 4 - A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

def poli(t):
	return int(str(t)[::-1]) == t

z = 0
for x in range(999, 99, -1):
    for y in range(x, 99 , -1):
        prod = x * y
        if poli(prod) and prod > z:
            z = prod

print(z)
