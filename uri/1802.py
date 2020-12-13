
livrosP = list(map(int, input().split()))
p = livrosP.pop(0)

livrosM = list(map(int, input().split()))
m = livrosM.pop(0)

livrosF = list(map(int, input().split()))
f = livrosF.pop(0)

livrosQ = list(map(int, input().split()))
q = livrosQ.pop(0)

livrosB = list(map(int, input().split()))
b = livrosB.pop(0)

conjuntos = int(input())

somas = []

for i in range(p):
    for j in range(m):
        for k in range(f):
            for l in range(q):
                for r in range(b):
                    somas.append(livrosP[i] + livrosM[j] + livrosF[k] + livrosQ[l] + livrosB[r])

somas.sort(reverse=True)
print(sum(somas[0:conjuntos]))
