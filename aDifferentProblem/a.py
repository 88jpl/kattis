import sys

for line in sys.stdin:
	if 'Exit' == line.rstrip():
		break
	else:
		txt = line.split()
		print(abs(int(txt[0]) - int(txt[1])))
