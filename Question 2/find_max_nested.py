def MaxArray(arr):
	if len(arr) is 0:
		raise Exception("Cannot find maximum value in an empty array!")
	return find_max_value_in_nested_list(arr, 0)

def find_max_value_in_nested_list(arr, max_value_till_now):
	for item in arr:
		if (isinstance(item, list)):
			max_value_till_now = find_max_value_in_nested_list(item, max_value_till_now)
		else:
			if item > max_value_till_now:
				max_value_till_now = item
	return max_value_till_now



if __name__ == "__main__":
	arr = [[141,151,161],2,3,[101,202,[303,404]]]
	# arr = []
	print(MaxArray(arr))