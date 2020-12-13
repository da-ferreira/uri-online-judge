
n, k = map(int, input().split())

envelopes = list(map(int, input().split()))

menor = float('inf')

envelopes.sort()
temp = i = 0

todos = []

while i < n:

    if i < n - 1 and envelopes[i] == envelopes[i + 1]:
        temp += 1

    else:
        todos.append(envelopes[i])
        temp += 1
        if temp < menor:
            menor = temp
        temp = 0

    i += 1

if len(todos) == k:
    print(menor)
else:
    print(0)
