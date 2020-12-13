
casos = int(input())

for i in range(casos):
    raj, she = input().split()

    if (raj == 'tesoura' and she == 'papel') or (raj == 'papel' and she == 'pedra') or (raj == 'pedra' and she == 'lagarto') \
        or (raj == 'lagarto' and she == 'spock') or (raj == 'spock' and she == 'tesoura') or (raj == 'tesoura' and she == 'lagarto') \
            or (raj == 'lagarto' and she == 'papel') or (raj == 'spock' and she == 'papel') or (raj == 'spock' and she == 'pedra') \
                or (raj == 'pedra' and she == 'tesoura'):
        print('rajesh')

    elif (raj == 'papel' and she == 'tesoura') or (raj == 'pedra' and she == 'papel') or (raj == 'lagarto' and she == 'pedra') \
        or (raj == 'spock' and she == 'lagarto') or (raj == 'tesoura' and she == 'spock') or (raj == 'lagarto' and she == 'tesoura') \
            or (raj == 'papel' and she == 'lagarto') or (raj == 'papel' and she == 'spock') or (raj == 'pedra' and she == 'spock') \
                or (raj == 'tesoura' and she == 'pedra'):
        print('sheldon')
    else:
        print('empate')
