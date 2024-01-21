n = int(input())
listOfJavilins = []
for i in range(n):
    new_jav = int(input())
    listOfJavilins.append(new_jav)


print(sum(listOfJavilins) - (n-1))
