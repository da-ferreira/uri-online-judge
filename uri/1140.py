
while True:
	senteca = input().lower().split()
	if senteca[0] == '*':
		break

	tautograma = 0
	for i in range(len(senteca)):
		if senteca[0][0] == senteca[i][0]:
			tautograma += 1
	tamanho_sent = len(senteca)

	if tautograma == tamanho_sent:
		print('Y')
	else:
		print('N')
