def extractUpper(sen):
	merged = ""
	for letter in range(len(sen)):
		if sen[letter].isupper():
			merged += sen[letter]
	return merged

string_1 = input("Enter string 1: ")
string_2 = input("Enter string 2: ")

result_string_1 = extractUpper(string_1)
result_string_2 = extractUpper(string_2)

final_string =  result_string_1 + result_string_2
print(final_string)