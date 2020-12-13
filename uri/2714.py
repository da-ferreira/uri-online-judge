
casos = int(input())

for i in range(casos):
    ra = input()
    if (len(ra) == 20) and (ra[0:2] == 'RA'):
        ra = ra.replace('RA', '')
        print(int(ra))
    else:
        print('INVALID DATA')
