
while True:
	nums = input().split(' ')
	x = int(nums[0])
	y = int(nums[1])

	if x == y:
		break
	if x > y:
		print('Decrescente')
	else:
		print('Crescente')
