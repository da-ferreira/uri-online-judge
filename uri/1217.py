
dias = int(input())
soma_compra = consumo_kg = 0

for i in range(dias):
    valor_gasto = float(input())
    frutas = input().split()

    soma_compra += valor_gasto
    consumo_kg += len(frutas)

    print('day {}: {} kg'.format(i+1, len(frutas)))

print('{:.2f} kg by day'.format(consumo_kg / dias))
print('R$ {:.2f} by day'.format(soma_compra / dias))
 