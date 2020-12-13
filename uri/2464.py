
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
permutacao = input()

criptografada = list(input())

for i in range(len(criptografada)):
    criptografada[i] = permutacao[alfabeto.index(criptografada[i])]

print(''.join(criptografada))
