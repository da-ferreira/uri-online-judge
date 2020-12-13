
quantidade = int(input())
emails = set()

for i in range(quantidade):
    email = input()
    email = list(email.partition('@'))

    primeira_parte = ''

    for j in range(len(email[0])):
        if email[0][j] != '.' and email[0][j] != '+':
            primeira_parte += email[0][j]
        else:
            if email[0][j] == '+':
                break
    
    email[0] = primeira_parte

    emails.add(''.join(email))

print(len(emails))
