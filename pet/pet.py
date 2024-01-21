lead_score = 0
leader = 0
for n in range(5):
    scores = input()
    scores = scores.split()
    sum_scores = sum(map(int, scores))
    if sum_scores > lead_score:
        lead_score = sum_scores
        leader = n + 1
    else:
        continue

print(leader, lead_score)


