
valor = int(input())

cem = valor // 100
temporaria = valor % 100

cinquenta = temporaria // 50
temporaria %= 50

vinte = temporaria // 20
temporaria %= 20

dez = temporaria // 10
temporaria %= 10

cinco = temporaria // 5
temporaria %= 5

dois = temporaria // 2
temporaria %= 2

um = temporaria // 1

print(valor)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cinquenta))
print('{} nota(s) de R$ 20,00'.format(vinte))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))
