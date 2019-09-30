def collatz(num):
	if num == 1:
		return 0
	step = 0
	while num != 1:
		if not num % 2:
			num //= 2
		else:
			num = num * 3 + 1
		step += 1
	return step

def find_collatz(num):
	ans = 0
	table = {}
	for i in range(2, num + 1):
		temp_res = 0
		temp_i = i
		while i != 1:
			if table.get(i, 0):
				temp_res += table[i]
				break
			else:
				if not i % 2:
					i //= 2
				else:
					i = i * 3 + 1
				temp_res += 1
		table[temp_i] = temp_res
	return max(0, max(table.values()))

if __name__ == '__main__':
	# num = 6
	# print(collatz(num))
	temp = 0
	for i in range(2, 10001):
		temp = max(temp, collatz(i))
	print(temp)
	print(find_collatz(10000))