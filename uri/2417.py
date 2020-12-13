
cor_vitoria, cor_empates, cor_saldo, fla_vitoria, fla_empates, fla_saldo = map(int, input().split()) 

if (cor_vitoria * 3 + cor_empates) > (fla_vitoria * 3 + fla_empates):
    print('C')

elif (cor_vitoria * 3 + cor_empates) < (fla_vitoria * 3 + fla_empates):
    print('F')
else:
    if cor_saldo > fla_saldo:
        print('C')
    elif cor_saldo < fla_saldo:
        print('F')
    else:
        print('=')
