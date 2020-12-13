
instancias = int(input())

for i in range(instancias):
    n = int(input())
    conjuntos = [0]

    for j in range(n):
        temp = list(map(int, input().split()))
        temp.pop(0)
        conjuntos.append(set(temp))

    q = int(input())

    for j in range(q):
        modo, set1, set2 = map(int, input().split())
        
        if modo == 1:
            print(len(conjuntos[set1] & conjuntos[set2]))
        else:
            print(len(conjuntos[set1] | conjuntos[set2]))
