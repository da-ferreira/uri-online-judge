
casos = int(input())

for i in range(casos):
    a, b, c, d = map(int, input().split())

    taxa = d - b
    taxa /= (c - a)

    taxa = str(taxa)
    taxa = taxa[0:taxa.index('.') + 3]
    taxa = taxa.replace('.', ',')

    if len(taxa[taxa.index(',') + 1:]) == 1:
        taxa += '0'

    print(taxa)
