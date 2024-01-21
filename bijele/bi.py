n = input()
n = n.split()
mapped = list(map( int, n))
answer = []
for i in range(2):
    if mapped[i] == 1:
        answer.append(0)
    elif mapped[i] > 1:
        diff = mapped[i] - 1
        diff *= -1
        answer.append(diff)
        diff = 0
    else:
        answer.append(1)
for i in range(2, 5):
    if mapped[i] == 2:
        answer.append(0)
    elif mapped[i] > 2:
        diff = mapped[i] - 2
        diff *=  -1
        answer.append(diff)
        diff = 0
    elif mapped[i] == 1:
        answer.append(1)
    else:
        answer.append(2)
if mapped[5] == 8:
    answer.append(0)
elif mapped[5] > 8:
    diff = mapped[5] - 8
    diff *= -1
    answer.append(diff)
    diff = 0
else:
    diff = 8 - mapped[5] 
    answer.append(diff)
    diff = 0


print(*answer)
