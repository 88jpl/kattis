prop = int(input())
listP = input().split()
ref = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 5, "9": 4, "10": 3, "11": 2, "12": 1}
total = 0
for i in listP:
	total += ref[i]
print(total/36)
