txt = input().split()
cr = int(txt[0])
bt = int(txt[1])
need = 0
for i in range(cr):
	req = int(input())
	need += req
if bt >= need:
	print("Jebb")
else:
	print("Neibb")
