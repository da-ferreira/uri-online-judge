
alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J','K', 'L',
    'M', 'N', 'O','P', 'Q', 'R',
    'S', 'T','U', 'V', 'W', 'X', 
    'Y', 'Z'
]

casos = int(input())

for i in range(casos):
    linhas = int(input())
    
    soma = 0

    for j in range(linhas):
        string = input()

        for k in range(len(string)):
            soma += alfabeto.index(string[k]) + k + j
    
    print(soma)
