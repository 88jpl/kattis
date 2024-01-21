ws = int(input())
c = int(input())
result = []
for i in range(c):
	txt = input().split()
	if int(txt[1]) < ws:
		result.append("{} lokud".format(txt[0]))
	else:
		result.append("{} opin".format(txt[0]))
for i in result:
	print(i)
