
n = int(input())
idiomas = {}

for i in range(n):
    pais = input()
    feliz_natal = input()

    idiomas[pais] = feliz_natal

m = int(input())

for i in range(m):
    nome_crianca = input()
    pais = input()
   
    print(nome_crianca)
    print(idiomas[pais])
    print()
