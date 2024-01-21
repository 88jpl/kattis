n = int(input())
answer = []
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        addToList = ( str(number) + ' is even')
        answer.append(addToList)
    else:
        addToList = ( str(number) + ' is odd')
        answer.append(addToList)
print(*answer, sep = '\n')
