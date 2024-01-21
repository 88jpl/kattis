n = int(input())
volume = 7
for i in range(n):
    choice = input()
    if choice == 'Skru op!':
        if volume < 10:
            volume += 1
        else:
            pass
    else:
        if volume > 0:
            volume -= 1
        else:
            pass
print(volume)

