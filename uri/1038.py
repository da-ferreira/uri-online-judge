tabela = [
		  [1, 'Cachorro Quente', 4.00],
		  [2, 'X-Salada', 4.50],
		  [3, 'X-Bacon', 5.00],
		  [4, 'Torrada simples', 2.00],
		  [5, 'Refrigerante', 1.50]
]

itens = input().split(' ')
codigo = int(itens[0])
quantidade = int(itens[1])

total = tabela[codigo-1][2] * quantidade  # <- Pegando o preço do item na tabela e multiplicando conforme sua quantidade.

print('Total: R$ {:.2f}'.format(total))
