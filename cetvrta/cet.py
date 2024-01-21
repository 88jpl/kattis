xcoords = []
ycoords = []
for i in range(3):
	coord = input()
	scoord = coord.split()
	#print(coord)
	xcoords.append(int(scoord[0]))
	ycoords.append(int(scoord[1]))
#print(xcoords, ycoords)
for i in xcoords:
	if xcoords.count(i) < 2:
		x = i	
for i in ycoords:
	if ycoords.count(i) < 2:
		y = i
print(x, y)
