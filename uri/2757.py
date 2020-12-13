
a = int(input())
b = int(input())
c = int(input())

a = str(a); b = str(b); c = str(c)

print(f'A = {a}, B = {b}, C = {c}')
print(f'A = {a.rjust(10, " ")}, B = {b.rjust(10, " ")}, C = {c.rjust(10, " ")}')

if int(a) > 0 and int(b) > 0 and int(c) > 0:
    print(f'A = {a.rjust(10, "0")}, B = {b.rjust(10, "0")}, C = {c.rjust(10, "0")}')
else:
    if int(a) < 0 and int(b) < 0 and int(c) < 0:
         print(f'A = {"-" + a.rjust(9, "0")}, B = {"-" + b.rjust(9, "0")}, C = {"-" + c.rjust(9, "0")}')
    elif int(a) < 0:
        temp = a.replace('-', '')
        print(f'A = {"-" + temp.rjust(9, "0")}, B = {b.rjust(10, "0")}, C = {c.rjust(10, "0")}')
    elif int(b) < 0:
        temp = b.replace('-', '')
        print(f'A = {temp.rjust(10, "0")}, B = {"-" + b.rjust(9, "0")}, C = {c.rjust(10, "0")}')
    elif int(c) < 0:
        temp = c.replace('-', '')
        print(f'A = {temp.rjust(10, "0")}, B = {b.rjust(10, "0")}, C = {"-" + c.rjust(9, "0")}')
print(f'A = {a.ljust(10, " ")}, B = {b.ljust(10, " ")}, C = {c.ljust(10, " ")}')

