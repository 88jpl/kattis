first_line = input(str())
parameters = first_line.split()

N = int(parameters[0])
MAX_SIZE = (int(parameters[1]) **2 + int(parameters[2]) **2) ** 0.5
while N > 0:
    match = int(input())
    if match <= MAX_SIZE:
        N -= 1
        print("DA")
    else:
        N -= 1
        print("NE")
