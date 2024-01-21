n = int(input())
for i in range(n):
    x = input()
    if x == 'P=NP':
        print('skipped')
    else:
        print(int(x[0]) + int(x[2]))
