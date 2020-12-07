
x = int(input())
z = int(input())

while z <= x:
    z = int(input())

valores = [x]
temp = x
soma = x

while soma <= z:
    temp += 1
    soma += temp
    valores.append(soma)
print(len(valores))
