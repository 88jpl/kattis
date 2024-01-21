stocks = int(input())
total = 0
for i in range(stocks):
	buys = int(input())
	lastBuy = (0, 0)
	for j in range(buys):
		buy = input().split()
		if int(buy[1]) > lastBuy[1]:
			total += int(buy[0])
			if lastBuy[1] != 0:
				total -= lastBuy[0]
			lastBuy = (int(buy[0]), int(buy[1]))
print(total)		
