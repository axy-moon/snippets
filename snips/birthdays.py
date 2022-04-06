birthdays = {'Aashee':'Jun 10','Sharone':'Apr 20','Figo':'Sep 8','Damian':'Feb 26'}

while True:
	name = input("Enter your name(Enter to Exit): ")

	if name == '':
		break
	if name in birthdays:
		print("Your birthday is " + birthdays[name])
	else:
		print('Your data is not entered.Please enter your bdate Information ->')
		bday = input()

	birthdays[name] = bday		