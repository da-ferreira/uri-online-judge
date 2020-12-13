
notas = list(input())
grades = []

while len(notas) != 0:
    if len(notas) != 1:
        if int(notas[0]) == 1 and int(notas[1]) == 0:
            grades.append(10)
            notas.pop(0); notas.pop(0)
        else:
            grades.append(int(notas[0]))
            notas.pop(0)
    else:
        grades.append(int(notas[0]))
        notas.pop(0)

print(f'{sum(grades) / len(grades) :.2f}')
