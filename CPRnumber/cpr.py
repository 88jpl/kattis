cpr = input()
values = [4,3,2,7,6,5,0,4,3,2,1]
total = 0
for i, num in enumerate(cpr):
	#print("index" + str(i))
	#print("number" + str(num) + " value: " + str(values[i]))
	if i == 6:
		pass
	else:
		value = int(num) * values[i]
		total += value
if total % 11 == 0:
	print(1)
else:
	print(0)	
