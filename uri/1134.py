
alcool = gasolina = diesel = 0
while True:
    combustivel = int(input())
    while combustivel not in range(1, 5):
        combustivel = int(input())
    if combustivel == 4:
        break

    if combustivel == 1:
        alcool += 1
    if combustivel == 2:
        gasolina += 1
    if combustivel == 3:
        diesel += 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))
