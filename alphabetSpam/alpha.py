txt = input()
white = 0
lower = 0
upper = 0
other = 0
for i in txt:
	if i == "_":
		white += 1
	elif i.islower():
		lower += 1
	elif i.isupper():
		upper += 1
	else:
		other += 1
length = len(txt)
print(white/length)
print(lower/length)
print(upper/length)
print(other/length)
