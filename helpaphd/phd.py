import sys
n = int(input())
answers = []
for i in range(n):
    problem = input()
    splitProblem = problem.split('+')
    a = problem[0]
    if a == 'P':
        answers.append('skipped')
    else:
        b = problem[-1]
        answers.append(int(a) + int(b))
print(*answers, sep = '\n')
