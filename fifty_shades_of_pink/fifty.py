n = int(input())
total = 0
for line in range(n):
    box_title = str(input()).lower()
    if (box_title.find('pink') != -1):
        total += 1
        #print(total)
    elif (box_title.find('rose') != -1):
        total += 1

    else:
        continue

if total == 0:
    print('I must watch Star Wars with my daughter')

else:
    print(total)
