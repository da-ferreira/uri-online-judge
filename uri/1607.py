
alfabeto = 'abcdefghijklmnopqrstuvwxyza'
casos = int(input())

for i in range(casos):
    string_a, string_b = input().split()
    string_a = list(string_a)
    string_b = list(string_b)
    
    operacoes = 0

    for j in range(len(string_a)):
        while string_a[j] != string_b[j]:
            string_a[j] = alfabeto[alfabeto.index(string_a[j])+1]
            operacoes += 1

    print(operacoes)
