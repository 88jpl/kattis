txt = input().split()
n = int(txt[0])
d = txt[1]
domD = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
nonDomD = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
total = 0
for i in range(4*n):
	hand = input()
	if hand[1] == d:
		total += domD[hand[0]]
	else:
		total += nonDomD[hand[0]]
print(total)
