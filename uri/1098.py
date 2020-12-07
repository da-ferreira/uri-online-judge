
i = 0
j1 = 1
j2 = 2
j3 = 3
for k in range(11):
    if k == 5 or k == 10:
        print('I={} J={}'.format(round(i), round(j1)))
        print('I={} J={}'.format(round(i), round(j2)))
        print('I={} J={}'.format(round(i), round(j3)))

    else:    
        print('I={} J={}'.format(round(i, 1), round(j1, 1)))
        print('I={} J={}'.format(round(i, 1), round(j2, 1)))
        print('I={} J={}'.format(round(i, 1), round(j3, 1)))

    i += 0.2
    j1 += 0.2
    j2 += 0.2
    j3 += 0.2

