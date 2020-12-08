
casos = int(input())

for i in range(casos):
    word = input()

    if len(word) == 3:
        teste1 = 'o' + word[1:]
        teste2 = word[0] + 'n' + word[2]
        teste3 = word[0:2] + 'e'

        if teste1 == 'one' or teste2 == 'one' or teste3 == 'one':
            print(1)
        else:
            print(2)
    else:
        print(3)
