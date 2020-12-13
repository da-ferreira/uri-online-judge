
conector1 = list(map(int, input().split()))
conector2 = list(map(int, input().split()))

veracidade = 0
for i in range(5):
    if conector1[i] != conector2[i]:
        veracidade += 1

if veracidade == 5:
    print('Y')
else:
    print('N')
