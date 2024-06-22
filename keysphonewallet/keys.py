n = int(input())
g = ["keys", "phone", "wallet"]
for i in range(n):
	item = input()
	if item in g:
		g.remove(item)
if len(g) == 0:
	print("ready")
else:
	for i in g:
		print(i)
