n = input().split('-')
answer = ''
for i in range(len(n)):
    word = n[i]
    letter = word[0]
    answer += letter
print(answer)

