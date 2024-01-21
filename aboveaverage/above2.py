n = int(input())
for i in range(n):
	line = input()
	splitLine = line.split()
	students = int(splitLine[0])
	passing = 0
	total = 0
	for student in range(1, students + 1):
		total += int(splitLine[student])
	average = total / students
	for student in range(1, students + 1):
		if int(splitLine[student]) > average:
			passing += 1
	result = (passing / students) * 100
	print("%.3f" % result + "%")

