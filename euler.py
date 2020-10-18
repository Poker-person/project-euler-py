# https://projecteuler.net/problem=2

# enconte a soma de todos os numeros naturais multiplos de 3 ou 5 ate 1000
#multiplos = []

#for i in range(1, 1000):
#    if (i % 3 == 0) or (i % 5 == 0):
#        multiplos.append(i)

#print(sum(multiplos))

# Encontre a soma dos numeros pares da sequencia de Fibonacci ate 4 milhoes

fibonacci_par = []

for i in range(0, 10):
    fibonacci_par.append(i + (i ** i))

print(fibonacci_par)
