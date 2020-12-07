
notas = input().split()

nota1 = float(notas[0]) * 2
nota2 = float(notas[1]) * 3
nota3 = float(notas[2]) * 4
nota4 = float(notas[3]) * 1

media = (nota1 + nota2 + nota3 + nota4) / 10
print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    media = (media + exame) / 2
    if media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media))
