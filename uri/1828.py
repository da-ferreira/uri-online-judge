
casos = int(input())

for i in range(casos):
    raj, she = input().split()

    if (raj == 'tesoura' and she == 'papel') or (raj == 'papel' and she == 'pedra') or (raj == 'pedra' and she == 'lagarto') \
        or (raj == 'lagarto' and she == 'Spock') or (raj == 'Spock' and she == 'tesoura') or (raj == 'tesoura' and she == 'lagarto') \
            or (raj == 'lagarto' and she == 'papel') or (raj == 'papel' and she == 'Spock') or (raj == 'Spock' and she == 'pedra') \
                or (raj == 'pedra' and she == 'tesoura'):
        print('Caso #{}: Bazinga!'.format(i+1))

    elif (raj == 'papel' and she == 'tesoura') or (raj == 'pedra' and she == 'papel') or (raj == 'lagarto' and she == 'pedra') \
        or (raj == 'Spock' and she == 'lagarto') or (raj == 'tesoura' and she == 'Spock') or (raj == 'lagarto' and she == 'tesoura') \
            or (raj == 'papel' and she == 'lagarto') or (raj == 'Spock' and she == 'papel') or (raj == 'pedra' and she == 'Spock') \
                or (raj == 'tesoura' and she == 'pedra'):
        print('Caso #{}: Raj trapaceou!'.format(i+1))
    else:
        print('Caso #{}: De novo!'.format(i+1))
