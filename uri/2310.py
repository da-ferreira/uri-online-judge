
jogadores = int(input())

geral = {
    'saques': 0,
    'bloqueios': 0,
    'ataques': 0,
    'saq_total': 0,
    'bloq_total': 0,
    'ataq_total': 0
}

for i in range(jogadores):
    nome = input()
    tentativas = list(map(int, input().split()))
    tentativas_certas = list(map(int, input().split()))

    
    geral['saques'] += tentativas_certas[0]
    geral['bloqueios'] += tentativas_certas[1]
    geral['ataques'] += tentativas_certas[2]

    geral['saq_total'] += tentativas[0]
    geral['bloq_total'] += tentativas[1]
    geral['ataq_total'] += tentativas[2]


print('Pontos de Saque: {:.2f} %.'.format(geral['saques']  * 100 / geral['saq_total']))
print('Pontos de Bloqueio: {:.2f} %.'.format(geral['bloqueios']  * 100 / geral['bloq_total']))
print('Pontos de Ataque: {:.2f} %.'.format(geral['ataques']  * 100 / geral['ataq_total']))
