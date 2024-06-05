n = int(input())
for i in range (n + 2):
	if i == 0:
		line = "+"
		for j in range(n):
			line += "-"
		line += "+"
		print(line)
		
	elif i == n + 1:
		line = "+"
		for j in range(n):
			line += "-"
		line += "+"
		print(line)
	else:
		line = "|"
		for j in range(n):
			line += " "
		line += "|"
		print(line)
