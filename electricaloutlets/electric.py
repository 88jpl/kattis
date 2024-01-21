n = int(input())
total = 1
answers = []
for n in range(n):
    raw_line = input()
    raw_split= raw_line.split()
    strips = int(raw_split[0])
#    print(raw_split)
#    print(strips)

    for i in range(strips):
        total -= 1
        total += int(raw_split[i+1])
    answers.append(total)
    total = 1
print(*answers, sep = '\n')
