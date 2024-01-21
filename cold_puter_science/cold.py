n = int(input())
data = input().split()
answer = 0
for n in data:
    if int(n) < 0:
        answer += 1
    else:
        continue
print(answer)

