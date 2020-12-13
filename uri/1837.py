
a, b = map(int, input().split())

q = a // abs(b)
if b < 0 and q > 0:
    q =  f'-{q}'

if a < 0 and b < 0:
    q = abs(q)

print(q, a % abs(b))
