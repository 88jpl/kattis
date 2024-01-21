from collections import Counter

dice = input().split()
rolls = []
for i in range(1, int(dice[0]) + 1):
	for j in range(1, int(dice[1]) + 1):
		#print(i + j)
		rolls.append(i + j)
count = Counter(rolls)
max = max(count.values())
#print(max)
nums = []
for i in count.items():
	if i[1] == max:
		nums.append(i[0])
for i in nums:
	print(i)
