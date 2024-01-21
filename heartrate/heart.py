n = int(input())
answers = []
for i in range(n):
    stats = input().split()
    beats = int(stats[0])
    seconds = float(stats[1])
    BPM = 60 * (beats/seconds)
    minABPM = BPM - (60 / seconds) 
    maxABPM = BPM + (60 / seconds)
    answers.append( str(round(minABPM, 4)) +' '+ str(round(BPM, 4)) +' '+ str(round(maxABPM, 4)))
print(*answers, sep = '\n')
