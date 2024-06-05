amountOfStudents = input()
listStudents = {}
for i in range(int(amountOfStudents)):
    listStudents[input()] = 0
numOfClasses = input()
for i in range(int(numOfClasses)):
    txt = input().split()
    for j in range(int(txt[0])):
        listStudents[txt[j + 1]] += 1
values = []
for i in listStudents:
    values.append(listStudents[i])
values.sort()
values.reverse()
for i in values:
    for j in listStudents:
        if listStudents[j] == i:
            print(str(listStudents[j]) + " " + j)
            listStudents.pop(j)
            break