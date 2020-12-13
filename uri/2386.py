
telescopio = int(input())
estrelas = 0

quantidade = int(input())

for i in range(quantidade):
    fotons = int(input())
    if fotons * telescopio >= 40000000:
        estrelas += 1
print(estrelas)
