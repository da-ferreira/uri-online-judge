
casos = int(input())

for i in range(casos):
    A, B = map(str, input().split())

    if A[-len(B):] == B:
        print('encaixa')    
    else:
        print('nao encaixa')
