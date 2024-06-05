txt = input().split()
r = int(txt[0])
c = int(txt[1])
zr = int(txt[2])
zc = int(txt[3])
for i in range(r):
	txt2 = input()
	result = ""
	if zr == 1 and zc == 1:
		print(txt2)
	else:
		if zc > 1:
			for j in txt2:
				result += j * zc
		print(result)
