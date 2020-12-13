
n = int(input())
medidas = list(map(int, input().split()))

veracidade = False
vales = picos = 0

for i in range(1, n):
    if medidas[i] > medidas[i - 1]:
        picos += 1
        vales = 0
    elif medidas[i] < medidas[i - 1]:
        vales += 1
        picos = 0
    
    if (medidas[i] == medidas[i - 1]) or (picos > 1) or (vales > 1):
        veracidade = True
        break
    
if veracidade:
    print(0)
else:
    print(1)
