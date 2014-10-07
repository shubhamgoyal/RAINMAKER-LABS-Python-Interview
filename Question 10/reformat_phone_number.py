LIST_DIGITS_AS_STRINGS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LIST_NON_DIGIT_VALID_CHARACTERS_AS_STRING = [' ', '-']

def ReformatPhoneNumber(number):
	if isPhoneNumberInvalid(number):
		raise Exception("Invalid phone number")
	return getDigitsFromNumber(number)

def isPhoneNumberInvalid(number):
	if (not doesPhoneNumberContainCorrectNumberOfDigits(number)) or doesNumberContainInvalidCharacters(number) or (doesNumberContainMoreThanOneSpaceOrHyphenTogether(number)) or (not areFirstAndLastCharactersNumber(number)):
		return True
	return False

def getDigitsFromNumber(number):
	number_without_spaces_and_hyphens = ''
	for char in number:
		if char in LIST_DIGITS_AS_STRINGS:
			number_without_spaces_and_hyphens = number_without_spaces_and_hyphens + char
	return number_without_spaces_and_hyphens

def doesPhoneNumberContainCorrectNumberOfDigits(number):
	num_digits_in_number = 0
	for char in number:
		if char in LIST_DIGITS_AS_STRINGS:
			num_digits_in_number = num_digits_in_number + 1
	if (num_digits_in_number >= 7) and (num_digits_in_number <= 12):
		return True
	else:
		False

def doesNumberContainInvalidCharacters(number):
	for char in number:
		if (char not in LIST_DIGITS_AS_STRINGS) and (char not in LIST_NON_DIGIT_VALID_CHARACTERS_AS_STRING):
			return True
	return False

def doesNumberContainMoreThanOneSpaceOrHyphenTogether(number):
	for i in range(0, len(number)):
		if i == 0:
			pass
		elif (number[i] in LIST_NON_DIGIT_VALID_CHARACTERS_AS_STRING) and (number[i - 1] in LIST_NON_DIGIT_VALID_CHARACTERS_AS_STRING):
			return True
	return False

def areFirstAndLastCharactersNumber(number):
	return (number[0] in LIST_DIGITS_AS_STRINGS) and (number[-1] in LIST_DIGITS_AS_STRINGS)

if __name__ == "__main__":
	print(ReformatPhoneNumber('012-345 69'))
	# print(ReformatPhoneNumber('012345'))
	# print(ReformatPhoneNumber('-012345 678'))
	# print(ReformatPhoneNumber('01203- 34566'))
	# print(ReformatPhoneNumber('123456678875432'))
	# print(ReformatPhoneNumber('1234x567'))