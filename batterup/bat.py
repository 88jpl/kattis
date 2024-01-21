n = int(input())
stats = input()
statsList = stats.split()
walks = 0
for i in range(n):
    if int(statsList[i]) == -1:
        walks += 1
    else:
        continue
stats = stats.replace("-1", "").split()
sumStats = sum(map(int, stats))
print(sumStats/(n-walks))
