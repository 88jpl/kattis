lane = int(input())
depth = int(input())
empty = 0
for i in range(depth):
	traffic = input()
	for j in traffic:
		if j == ".":
			empty += 1
print(empty / (lane * depth))	
