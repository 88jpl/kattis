n = int(input())
answers = []
for i in range(n):
    line = input().split()
    place = line[0]
    days = int(line[1])
    total = 0
    for d in range(days):
        candles = d+2
        total += candles
    answer = place + ' ' + str(total)
    answers.append(answer)
#print(answers)
print(*answers, sep = '\n')
