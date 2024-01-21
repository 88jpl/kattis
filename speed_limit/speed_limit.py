n = int(input())
answers = []
while n != -1:
    total = 0
    previous = 0
    for i in range(n):
        times = input().split()
        times = list(map(int, times))
        previous = times[1] - previous
        total += times[0] * previous
        previous = times[1]
    answers.append(str(total) + ' miles')
    total = 0
    n = int(input())
the_way =list(map(str, answers))
#print(the_way)
#print(*the_way)
print( *the_way , sep = "\n")

