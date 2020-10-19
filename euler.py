# https://projecteuler.net/problem=2

# enconte a soma de todos os numeros naturais multiplos de 3 ou 5 ate 1000
#multiplos = []

#for i in range(1, 1000):
#    if (i % 3 == 0) or (i % 5 == 0):
#        multiplos.append(i)

#print(sum(multiplos))

# Encontre a soma dos numeros pares da sequencia de Fibonacci ate 4 milhoes
x1 = 0
x2 = 0
fibonacci_par = []

for i in range(1, 4000000):
    x2 = x2 + x1
    x1 = x2 - x1
    if x2 == 0:
        x2 = x2 + 1
    if x1 % 2 == 0:
        fibonacci_par.append(x1)

print(sum(fibonacci_par))
