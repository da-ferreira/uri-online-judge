
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    postes = list(map(int, input().split()))
    result = 0

    for i in range(len(postes)):
        if i != (quantidade - 1):
            if postes[i] == 0 and postes[i+1] == 0:
                result += 1
                if i != (quantidade -2) and postes[i+2] == 1:
                    postes[i] = 1
                else:
                    postes[i+1] = 1  
        else:
            if postes[i] == 0 and postes[0] == 0:
                result +=1
    print(result)

