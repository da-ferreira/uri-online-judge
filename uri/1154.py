
idades = []
while True:
    age = int(input())
    if age < 0:
        break
    idades.append(age)

media = sum(idades) / len(idades)
print('{:.2f}'.format(media))
