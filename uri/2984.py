
assuntos = input()

pendentes = []

for i in range(len(assuntos)):
    if assuntos[i] == ')' and len(pendentes) > 0:
        pendentes.pop()
    elif assuntos[i] == '(':
        pendentes.append('(')

if len(pendentes) > 0:
    print(f'Ainda temos {len(pendentes)} assunto(s) pendente(s)!')
else:
    print('Partiu RU!')
