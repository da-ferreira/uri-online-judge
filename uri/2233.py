
r = int(input(), 16)
g = int(input(), 16)
b = int(input(), 16)

verdes = r // g
azuis = g // b

total = (verdes ** 2) * (azuis ** 2) + (verdes ** 2) + 1

print(hex(total)[2:])
