n = int(input())
answers = []
for i in range(n):
    stats = input()
    stats = stats.split()
    no_ad = int(stats[0])
    yes_ad = int(stats[1])
    cost = int(stats[2])
    profit = yes_ad - cost
    if profit == no_ad:
        answers.append('does not matter')
    elif profit > no_ad:
        answers.append('advertise')
    else:
        answers.append('do not advertise')

print(*answers, sep = '\n')
