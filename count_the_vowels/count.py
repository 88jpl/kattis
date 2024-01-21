n = input().lower()
answer = 0
for l in n:
    if l == 'a':
        answer += 1
    elif l == 'e':
        answer += 1
    elif l == 'o':
        answer += 1
    elif l == 'i':
        answer += 1
    elif l == 'u':
        answer += 1
    else:
        pass
print(answer)
