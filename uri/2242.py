
risada = input()
temp = ''

for i in range(len(risada)):
    if risada[i] in 'aeiou':
        temp += risada[i]

if temp == temp[-1::-1]:
    print('S')
else:
    print('N')
