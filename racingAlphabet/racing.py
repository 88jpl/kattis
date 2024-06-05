n = int(input())
dist = 60/28
alpha = {'A': 0, 'B': 1, 'C':2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26, '"': 27}
for i in range(n):
	note = input()
	for (j, l) in enumerate(note):
		print(len(note))
		if j == (len(note) - 1):
			break
		print(alpha.get(f"{l}"), j)
		print(abs(alpha.get(note[j + 1])  - alpha.get(f"{l}")))
