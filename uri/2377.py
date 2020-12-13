
estrada, pedagio = map(int, input().split())
km, preco_pedagio = map(int, input().split())

total = (estrada * km) + ((estrada // pedagio) * preco_pedagio)
print(total)
