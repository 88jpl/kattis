cost = input()
n = input()
totals = []
for n in range(int(n)):
    dim = input().split()
    dim = list(map(float, dim))
    w = dim[0]
    h = dim[1]
    area = w*h
    totals.append(area)

totalSum = sum(totals)
answer = totalSum * float(cost)
print(round(answer, 8))
