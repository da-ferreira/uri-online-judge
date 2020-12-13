
casos = int(input())

for i in range(casos):
    a, b = map(int, input().split())
    
    if a == b:
        print(a)
    else:
        print(1)
