numbers = input()
numbers = numbers.split()
n1 = int(numbers[0])
n2 = int(numbers[1])
n3 = int(numbers[2])
letters = input()
answers = ''
maxNum = 0
minNum = 101
for num in numbers:
    if int(num) > maxNum:
        maxNum = int(num)
    if int(num) < minNum:
        minNum = int(num)

mid = 0
for num in numbers:
    if int(num) != minNum and int(num) != maxNum:
        mid = int(num)
for l in letters:
    if l == 'C':
        answers += str(maxNum)
    elif l == 'A':
        answers += str(minNum)
    else:
        answers += str(mid)
    answers += " "
print(answers)
