import math

n = input().split()
h = int(n[0])
v = math.radians(int(n[1]))
answer = (h /math.sin(v))
#print(math.sin(v))
print(math.ceil(answer))
