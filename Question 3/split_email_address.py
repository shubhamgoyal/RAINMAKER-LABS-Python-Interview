def SplitEmailAddress(address):
	email_address_component_list = address.split('@')
	dict = {
		'user': email_address_component_list[0],
		'domain': email_address_component_list[1]
	}
	return dict

if __name__ == "__main__":
	dict = SplitEmailAddress('myuser_1@mailserver.example.com')
	print(dict)