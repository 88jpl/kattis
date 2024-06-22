b = input()[::-1]
count = 0
result = ""
temp = 0
for i in b:
	if count == 0:
		count += 1
		if int(i) == 1:
			temp += 1
	elif count == 1:
		count += 1
		if int(i) == 1:
			temp += 2
	else:
		count = 0
		if int(i) == 1:
			temp += 4
			result = str(temp) + result
			temp = 0
	print(temp, count, result)
print(result)
