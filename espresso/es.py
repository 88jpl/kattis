(n , s) = input().split()
tank = int(s)
refill = 0
for i in range(int(n)):
	order = input()
	cost = 0
	if "L" in order:
		cost += 1
		order = order.replace("L", "")
		cost += int(order)
	else:
		cost += int(order)
	if tank - cost > -1:
		tank -= cost
	else:
		refill += 1
		tank = int(s)
		tank -= cost
	#print(tank)
print(refill)	
