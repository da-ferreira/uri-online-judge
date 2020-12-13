
notas = list(map(float, input().split()))

notas.remove(max(notas))
notas.remove(min(notas))

print(f'{sum(notas) :.1f}')
