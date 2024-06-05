txt = input().split()
h = {}
for c in txt:
	#print(c[0])
	if h.get(c[0]) != None:
		h[c[0]] += 1
	else:
		h[c[0]] = 1
top = 1
for i in h:
	#print(h[i])
	if h[i] > top:
		top = h[i]
if top > 1:
	print(top)
else:
	print(1)	 
