
while True:
    try:
        quantidade, ano = map(int, input().split())
        nomes_diferentes = 0
        nomes = set()
        
        for i in range(quantidade):
            aluno = input().split()
            aluno = [x[0] for x in aluno]
            
            if ''.join(aluno) not in nomes:
                nomes.add(''.join(aluno))
            else:
                nomes_diferentes += 1
        
        print(nomes_diferentes)
    except EOFError:
        break
