numberOfKnots = int(input())
learn = input()
know = input()
all = []
for i in learn.split():
	all.append(i)
for i in know.split():
	all.append(i)
#print(all)
for i in range(numberOfKnots):
	theCount = all.count(all[i])
	if theCount < 2:
		print(all[i])
