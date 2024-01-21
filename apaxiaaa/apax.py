n = input()
answer = ''
previous = ''
for i in n:
    
    #print(previous)
    if i == previous:
        pass
    else:
        answer += i
        previous = i
print(answer)
