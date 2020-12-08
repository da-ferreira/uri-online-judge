
j = 0
while True:
    bissexto = huluculu = bulukulu = False
    try:
        ano = int(input())

        if j != 0:
            print()

        if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
            print('This is leap year.')
            bissexto = True 
        
        if ano % 15 == 0:
            print('This is huluculu festival year.')
            huluculu = True
        
        if bissexto:
            if ano % 55 == 0:
                print('This is bulukulu festival year.')
                bulukulu = True
        if (not bissexto) and (not huluculu) and (not bulukulu):
            print('This is an ordinary year.')
        j += 1
    except EOFError:
        break

    