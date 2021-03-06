
bolinhas = int(input())
galhos = int(input())

if galhos / 2 > bolinhas:
    print(f'Faltam {galhos // 2 - bolinhas} bolinha(s)')
else:
    print(f'Amelia tem todas bolinhas!')