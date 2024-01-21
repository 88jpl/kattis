n = input()
changes = 0
count = 0
for i in range(0, len(n), 3):
	if n[i] != "P":
		count += 1
	if n[i + 1] != "E":
		count += 1
	if n[i + 2] != "R":
		count += 1
print(count)
