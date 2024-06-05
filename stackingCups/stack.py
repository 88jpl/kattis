n = int(input())
cups = {}
for i in range(n):
	txt = input().split()
	#print(txt[0])
	if txt[0][0].isalpha():
		cups[txt[0]] = int(txt[1])
	else:
		cups[txt[1]] = int(txt[0])//2
d = sorted(((v, k) for k, v in cups.items()))
#print(cups)
#print(d)
for i in d:
	print(i[1])
