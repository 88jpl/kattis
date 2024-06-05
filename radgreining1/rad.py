def rad():	
	(l, n) = input().split()
	result = ""
	for i in range(int(l)):
		result += "?"
	check = ["?"] * int(l)
	for i in range(int(n)):
		(loc, dna) = input().split()
		count = 0
		for j in range(int(loc) - 1, int(loc) + len(dna) - 1):
			if check[j] != "?" and check[j] != dna[count]:
				return "Villa"
			check[j] = dna[count]
			result = result[:j] + dna[count] + result[j + 1:]
			count += 1
	return result
print(rad())
