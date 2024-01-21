n = int(input())
answers = []
for n in range(n):
    catalog = {}
    tests = int(input())
    new = 0
    visits = []
    for i in range(tests):
        where = input()
        catalog[where] = 1
    answers.append(len(catalog))
print(*answers, sep = '\n')
