n = int(input())
c = 0
m = 0
h = 0
for i in range(n):
	txt = input().split()
	if txt[0] == "J":
		c += 1
	if txt[1] == "J":
		m += 1
	if txt[2] == "J":
		h += 1
totals = []
totals.append(c)
totals.append(m)
totals.append(h)
#print(c, m, h)
#print(totals)
print(min(totals))
		
