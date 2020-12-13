
while True:
    try:
        qtd_album, qtd_playlist = map(int, input().split())

        musicas = list(map(int, input().split()))
        sequencia = list(map(int, input().split()))

        i = tempo = 0
        tocadas = set()

        while i < qtd_playlist:

            if sequencia[i] not in tocadas:
                tocadas.add(sequencia[i])
                tempo += musicas[sequencia[i] - 1]
            else:
                tempo += musicas[sequencia[i] - 1]
            
            i += 1

            if len(tocadas) == qtd_album:
                break
                
        if len(tocadas) == qtd_album:
            print(tempo)
        else:
            print(-1)
    except EOFError:
        break
