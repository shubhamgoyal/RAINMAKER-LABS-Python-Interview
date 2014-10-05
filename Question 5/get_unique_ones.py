def GetUniqueOnes(arr):
	list_unique_integers = list(set(arr))
	str_rep_of_list = ','.join(map(str, list_unique_integers))
	return str_rep_of_list

if __name__ == "__main__":
	arr = [34,54,67,68,141,151,161,141,54,151,54]
	print(GetUniqueOnes(arr))