def GetLongestString(*args_list):
	if len(args_list) == 0:
		raise Exception("Can't return the length of the longest string if no string is passed as argument!")
	length_longest_string = 0
	for string in args_list:
		if len(string) > length_longest_string:
			length_longest_string = len(string)
	return length_longest_string

if __name__ == "__main__":
	print(GetLongestString("a", "aaa", "aa"))
	print(GetLongestString("a", "bcd", "efgh", "ij", ""))