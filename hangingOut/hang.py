(L, x) = input().split()
occu = 0
denied = 0
for i in range(int(x)):
	r = input().split()
	if r[0] == "enter":
		#print( r[1], L)
		if int(r[1]) + occu > int(L):
			denied += 1
		else:
			occu += int(r[1])		
	else:
		occu -= int(r[1])
	#print(occu)
print(denied)
