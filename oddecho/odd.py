n = int(input())
answers = []
for i in range(n):
    num = i + 1
    word = input()
    if num == 1:
        answers.append(word)
    elif num % 2 == 0:
        continue
    else:
        answers.append(word)
print(*answers, sep = '\n')
