
num = int(input())

if num % 2 == 1:
	for i in range(6):
		print(num)
		num += 2
else:
	for i in range(6):
		print(num+1)
		num += 2
