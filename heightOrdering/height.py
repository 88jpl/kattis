rounds = int(input())
for i in range(rounds):
	theHeights = input().split()
	count = 0
	orderedList = []
	stillSorting = True
	while stillSorting:
		stillSorting = False
		for j in range(1,20):
			if theHeights[j] > theHeights[j+1]:
				theHeights[j], theHeights[j+1] = theHeights[j+1], theHeights[j]
				count += 1
				stillSorting = True
		for j in range(19, 1, -1):
			if theHeights[j] > theHeights[j + 1]: 
				theHeights[j], theHeights[j+1] = theHeights[j+1], theHeights[j]
				count += 1
				stillSorting = True
	print(str(theHeights[0]) + " " + str(count))	
