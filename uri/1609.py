
casos = int(input())

for i in range(casos):
    qtd = int(input())
    carneiros = list(map(int, input().split()))
    
    print(len(set(carneiros)))
