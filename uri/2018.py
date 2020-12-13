
quadro_de_medalhas = []
paises_ordem = {}
paises_registrados = set()

def adicionar_medalhas(pais, i):
    global quadro_de_medalhas
    global paises_ordem


    if i == 0:
        quadro_de_medalhas[paises_ordem[pais]][1] += 1  # ouro
    elif i == 1:
        quadro_de_medalhas[paises_ordem[pais]][2] += 1  # prata
    else:
        quadro_de_medalhas[paises_ordem[pais]][3] += 1  # bronze


j = 0

while True:
    try:
        modalidade = input()

        for i in range(3):
            pais = input()

            if pais not in paises_registrados:
                quadro_de_medalhas.append([pais, 0, 0, 0])
                paises_ordem[pais] = j 
                paises_registrados.add(pais)

                j += 1

                adicionar_medalhas(pais, i)
            else:
                adicionar_medalhas(pais, i)
    except EOFError:
        break
    
quadro_de_medalhas.sort(key=lambda k: k[0])  # nome
quadro_de_medalhas.sort(key=lambda k: k[3], reverse=True)  # bronze
quadro_de_medalhas.sort(key=lambda k: k[2], reverse=True)  # prata
quadro_de_medalhas.sort(key=lambda k: k[1], reverse=True)  # ouro

print('Quadro de Medalhas')

for nome, ouro, prata, bronze in quadro_de_medalhas:
    print(nome, ouro, prata, bronze)
