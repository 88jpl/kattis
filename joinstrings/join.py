loop = int(input())
words = {}
for i in range(1, loop + 1):
	words["{}".format(i)] = input()
last = 0
#print(words)
for i in range(loop -1):
	op = input().split()
	#print(words["{}".format(op[0])], words["{}".format(op[1])])
	words[op[0]] = words[op[0]] + words[op[1]]
	words[op[1]] = ""
	last = op[0]
print(words[last])
