num = input()
temp = ""
for i in range(1, len(num)):
	if int(num[-(i + 1)]) < int(num[-i]):
		
		temp += num[-i]
		temp += num[-(i + 1)]
		print(temp)
		break
	
