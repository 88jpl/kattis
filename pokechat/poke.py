s = input()
key = input()
word = ""
for i in range(0,len(key), 3):
	num = key[i] + key[i + 1] + key[i +2]
	#print(num)
	num.lstrip('0')
	word += s[int(num) - 1]
print(word)
