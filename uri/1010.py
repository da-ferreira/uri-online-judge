peca1 = input().split(' ')
peca2 = input().split(' ')

total = (int(peca1[1]) * float(peca1[2])) + (int(peca2[1]) * float(peca2[2]))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
