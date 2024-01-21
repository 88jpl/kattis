m = input()
b = 1
for i in m:
	#print(i)
	if i == "A":
		if b == 1:
			b = 2
		elif b == 2:
			b = 1
	elif i == "B":
		if b == 2:
			b = 3
		elif b == 3:
			b = 2
	elif i == "C":
		if b == 1:
			b = 3
		elif b == 3:
			b = 1
print(b)
