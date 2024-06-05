n = int(input())
result = "impossible"
g = 0
for i in range(n):
	room = input().split()
	g += int(room[0])
	if g <  int(room[1]):
		result = "impossible"
		break
	else:
		result = "possible" 
print(result)
