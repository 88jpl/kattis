width = int(input())
pieces = int(input())
answers = []

for i in range(pieces):
    size = input().split()
    w = int(size[0])
    l = int(size[1])
    area = w*l
    answers.append(area)
print(int(sum(answers)/width))
