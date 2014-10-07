if __name__ == "__main__":
	num = 200
	list_multiples_8 = []
	while (num <= 600):
		if num % 8 == 0:
			list_multiples_8.append(num)
			num = num + 8
		else:
			num = num + 1
	print(','.join(map(str,list_multiples_8)))