t = input().split()
hc = False
h = int(t[0])
m = int(t[1])
if m - 45 < 0:
	if h == 0:
		h = 23
	else:
		h -= 1
	m -= 45
	m += 60
else:
	m -= 45
print("{} {}".format(h, m))
