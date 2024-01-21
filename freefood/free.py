n = int(input())
free = {}
for i in range(n):
    days = input()
    days = days.split()
    for d in range(int(days[0]),int(days[1])+1):
#        print(d)
        free[d] = 1

print(len(free))
