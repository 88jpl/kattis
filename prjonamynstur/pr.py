txt = input().split()
r = int(txt[0])
c = int(txt[1])
p = ""
l = 0
for i in range(r):
	p += input()
l += p.count(".") * 20
l += p.count("O") * 10
l += p.count("\\") * 25
l += p.count("/") * 25
l += p.count("A") * 35
l += p.count("^") * 5
l += p.count("v") * 22
print(l)
