
atraso_m, reacao_m, escrita_m = map(int, input().split())
atraso_v, reacao_v, escrita_v = map(int, input().split())

frase = input()

tempo_m = (2 * atraso_m) + reacao_m + (escrita_m * len(frase)) 
tempo_v = (2 * atraso_v) + reacao_v + (escrita_v * len(frase))

if tempo_m < tempo_v:
    print('Matheus')
elif tempo_m > tempo_v:
    print('Vinicius')
else:
    print('Empate')
    