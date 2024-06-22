word = input()
out = input()
count = 1
for i in range(len(word)):
	if word[i] != out[i]:
		count += 1
print(count)
