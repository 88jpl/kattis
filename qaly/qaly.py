n = int(input())
totals =  []
for n in range(n):
    stats = input().split(' ')
    answer = float(stats[0]) * float(stats[1])
    totals.append(answer)
num = sum(totals)

print('%.3f' %num)
