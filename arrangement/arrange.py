rooms = int(input())
teams = int(input())
lines = teams // rooms
add = teams % rooms
for i in range(rooms):
    answer = lines
    if add > 0:
        answer += 1
        add -= 1
        print('*' * answer)
    else:
        print('*' * answer)
