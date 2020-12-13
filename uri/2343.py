
n = int(input())

mito = False
raios = {}

for i in range(n):
    xy = input()
    if xy not in raios:
        raios[xy] = 1
    else:
        mito = True

if mito:
    print(1)
else:
    print(0)
