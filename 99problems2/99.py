setup = input().split()
n = int(setup[0])
q = int(setup[1])
probs = input().split()
for i in range(q):
	response = input().split()
	a = int(response[0])
	p = response[1]
	if a == 1:
		for j in probs:
			if j > p:
				print(max(probs)
				probs.remove(max(probs))
				break
			else:
				print(-1)
