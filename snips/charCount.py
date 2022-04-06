message = input("Enter the string: ")

count = {}

for chars in message:
	count.setdefault(chars,0)
	count[chars] = count[chars] + 1
print(count)	