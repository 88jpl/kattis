n = input().split()
x = int(n[0])
y = int(n[1])
z = int(n[2])
answers = []
for i in range(z):
    num = i + 1
    if num % x == 0:
        if num % y == 0:
            answers.append('FizzBuzz')
        else:
            answers.append('Fizz')
    elif num % y == 0:
        answers.append('Buzz')
    else:
        answers.append(num)
print(*answers, sep = '\n')
