banned = input()
txt = input().split()
answer = ""
for index, i in enumerate(txt):
	ban = False
	for j in banned:
		#print(i, i.count(j))
		if i.count(j) > 0:
			ban = True
			break
	if ban: 
		tmp = ""
		for j in i:
			tmp += "*"
		if index < len(txt) - 1:
			tmp += " "
		answer += tmp
	else:
		answer += i
		if index < len(txt) - 1:
			answer += " "
print(answer)
