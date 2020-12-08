
while True:
    bilhete_original, pessoas = map(int, input().split())
    if bilhete_original == 0 and pessoas == 0:
        break

    bilhetes = list(map(int, input().split()))
    bilhetes.sort()

    repetidos = 0

    while len(bilhetes) != 0:
        if bilhetes.count(bilhetes[0]) > 1:
            repetidos += 1
            for i in range(bilhetes.count(bilhetes[0])):
                bilhetes.pop(0)
        else:
            for i in range(bilhetes.count(bilhetes[0])):
                bilhetes.pop(0)
    
    print(repetidos)
