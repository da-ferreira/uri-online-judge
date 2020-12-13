
a, b, c, d = map(int, input().split())

skills = [
    abs((a + b) - (c + d)),
    abs((a + c) - (b + d)),
    abs((a + d) - (b + c))
]

print(min(skills))
