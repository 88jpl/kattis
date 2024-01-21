para = input().split()
N = int(para[1])
n = int(para[1])
votes = int(para[0])
MAX = (votes - N) * 3
MIN = (votes - N) *-3
fmax = MAX
fmin = MIN

while n > 0:
    vote = int(input())
    fmax += vote
    fmin += vote
    n -= 1
theMIN = fmin / votes
theMAX = fmax / votes
print(theMIN, theMAX)
#print((fmin / votes) + " " + (fmax / votes))





