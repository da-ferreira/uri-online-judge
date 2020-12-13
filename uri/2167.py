
medidas = int(input())

rpm = list(map(int, input().split()))
queda = 0

for i in range(1, len(rpm)):
    if rpm[i] < rpm[i - 1]:
        queda = rpm.index(rpm[i]) + 1
        break

if queda != 0:
    print(queda)    
else:
    print(queda)
