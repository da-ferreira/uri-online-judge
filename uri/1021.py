
valor = float(input())

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
temporaria %= 1

centavo_50 = temporaria // 0.50
temporaria %= 0.50

centavo_25 = temporaria // 0.25
temporaria %= 0.25

centavo_10 = temporaria // 0.10
temporaria %= 0.10

centavo_5 = temporaria // 0.05
temporaria %= 0.05

centavo_1 = temporaria // 0.01

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int((dois))))

print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(centavo_50)))
print('{} moeda(s) de R$ 0.25'.format(int(centavo_25)))
print('{} moeda(s) de R$ 0.10'.format(int(centavo_10)))
print('{} moeda(s) de R$ 0.05'.format(int(centavo_5)))
print('{} moeda(s) de R$ 0.01'.format(int(centavo_1)))
    