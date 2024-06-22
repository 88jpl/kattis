n = int(input())
name = ""
score = 0
for i in range(n):
	txt = input().split()
	if int(txt[1]) > score:
		score = int(txt[1])
		name = txt[0]
print(name)
