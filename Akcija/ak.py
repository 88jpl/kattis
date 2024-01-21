times = int(input())
priceList = []
totalCost = 0
for i in range(times):
	book = int(input())
	priceList.append(book)
#print(priceList)
priceList.sort(reverse=True)
#print(priceList)
for b in range(0, len(priceList), 3):
	#print(priceList[b])
	totalCost += priceList[b]
for b in range(1, len(priceList), 3):
	#print(priceList[b])
	totalCost += priceList[b]
print(totalCost)		
