
numero = int(input())

termo1 = 0
termo2 = 1
fib = termo1 + termo2

sequencia = [str(termo2)]

for i in range(numero-1):
    sequencia.append(str(fib))
    
    termo1 = termo2
    termo2 = fib
    fib = termo1 + termo2

sequencia.reverse()
print(' '.join(sequencia))
