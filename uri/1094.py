
casos = int(input())

rato = sapo = coelho = total = 0
animais = []
for i in range(casos):
    animais.append(input())

for i in range(len(animais)):
    total += int(animais[i][:2])

    if animais[i][2:] in ' R':
        rato += int(animais[i][:2])
    elif animais[i][2:] in ' S':
        sapo += int(animais[i][:2])
    elif animais[i][2:] in ' C':
        coelho += int(animais[i][:2])

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format((coelho * 100) / total))
print('Percentual de ratos: {:.2f} %'.format((rato * 100) / total))
print('Percentual de sapos: {:.2f} %'.format((sapo * 100) / total))
