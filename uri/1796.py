
pessoas = int(input())
opiniao = list(map(int, input().split()))

porcentagem = (opiniao.count(0) * 100) / pessoas

if porcentagem > 50.0:
    print('Y')
else:
    print('N')
