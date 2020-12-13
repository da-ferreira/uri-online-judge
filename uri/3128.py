
idade1 = int(input())
idade2 = int(input())

if idade1 >= 6 and idade2 >= 6:
    if idade1 >= 18 or idade2 >= 18:
        print('YES')
    elif idade1 >= 14 and idade2 >= 14:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
