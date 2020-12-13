
projetos = 1

while True:
    try:
        inicial, final = map(float, input().split())
        
        taxa = ((final / inicial) - 1) * 100
        
        print('Projeto {}:'.format(projetos))
        print('Percentual dos juros da aplicacao: {:.2f} %'.format(taxa))
        print()

        projetos += 1
    except EOFError:
        break
