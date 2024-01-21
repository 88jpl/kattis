i = input()
dimensions = i.split()
length = int(dimensions[0])
h = int(dimensions[1])
v = int(dimensions[2])
if length - h > h:
	h = length - h
if length - v > v:
	v = length - v
print(h * v * 4)
