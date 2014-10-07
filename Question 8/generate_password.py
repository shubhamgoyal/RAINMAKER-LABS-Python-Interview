import random

def GeneratePassword(num_chars, string_chars):
	password = ''
	for i in range(0, num_chars):
		password = password + random.choice(string_chars)
	return password

if __name__ == "__main__":
	print(GeneratePassword(5, 'abc0123'))
	print(GeneratePassword(7,'abczxc012394'))