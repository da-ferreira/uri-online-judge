
def reajuste_salarial(salario):
	if (salario >= 0) and (salario <= 400.00):  # <- 15%
		novo = salario * 1.15
		reajuste = salario * 0.15
		percentual = '15 %'

	if (salario > 400) and (salario <= 800):  # <- 12%
		novo = salario * 1.12
		reajuste = salario * 0.12
		percentual = '12 %'

	if (salario > 800) and (salario <= 1200): # <- 10%
		novo = salario * 1.10
		reajuste = salario * 0.10
		percentual = '10 %'

	if (salario > 1200) and (salario <= 2000):  # <- 7%
		novo = salario * 1.07
		reajuste = salario  * 0.07
		percentual = '7 %'

	if salario > 2000:  # <- 4%
		novo = salario * 1.04
		reajuste = salario * 0.04
		percentual = '4 %'
	
	return [novo, reajuste, percentual]

salario = float(input())

aumento = reajuste_salarial(salario)

print('Novo salario: {:.2f}'.format(aumento[0]))
print('Reajuste ganho: {:.2f}'.format(aumento[1]))
print('Em percentual: {}'.format(aumento[2]))
