
num_char1, distancia_char1, velocidade_char1 = map(int, input().split()) 
num_char2, distancia_char2, velocidade_char2 = map(int, input().split())

if (distancia_char1 / velocidade_char1) < (distancia_char2 / velocidade_char2):
    print(num_char1)
else:
    print(num_char2)

