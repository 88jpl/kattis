n = int(input())
for i in range(n):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	txt = input()
	for c in txt:
		if c.isalpha():
			if c.lower() in alphabet:
				alphabet.remove(c.lower())
	#print(alphabet)
	if len(alphabet) > 0:
		result = ""
		for j in alphabet:
			result += j
		print("missing", result)
	else:
		print("pangram")
