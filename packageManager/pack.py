t = input().split()
inv = input().split()
master = {}
for i in range(int(t[0])):
	txt = input().split()
	master[txt[0]] = int(txt[1])
for i in range(int(t[1])):
	steps = 0
	for j in range(int(inv[i])):
		txt = input().split()
		steps += master[txt[0]] - int(txt[1])
	print(steps)
