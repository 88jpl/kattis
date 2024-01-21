s = input().split()
#print(s)
dups = False
for i in s:
	if s.count(i) > 1:
		dups = True
#print(dups)
if dups:
	print("no")
else:
	print("yes")
