g = int(input())
guesses = []
for i in range(g):
	guess = input().split()
	guesses.append((guess[0], guess[1]))
q = int(input())
for i in range(q):
	idea = int(input())
	closeValue = 100000000000
	closeName = None
	for g in guesses:
		if int(g[1]) <= idea and (idea - int(g[1])) < closeValue:
			closeValue = (idea- int(g[1]))
			closeName = g[0]
	if closeName == None:
		print(':(')
	else:
		print(closeName)
