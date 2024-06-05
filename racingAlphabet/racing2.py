from math import pi

n = int(input())
alphabet = [None, 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ', "'"]
#print(alphabet.index("'"))
for i in range(n):
	txt = input()
	total = len(txt)
	for j in range(1, len(txt)):
		#print(txt[j-1], txt[j])
		at = alphabet.index(txt[j - 1])
		dest = alphabet.index(txt[j])
		if dest < at:
			at, dest = dest, at
		run = min(dest - at, 28 - dest + at)
		time = (run * pi) / 7
		total += time
		#print(j, ": At: ", at, " , Dest: ", dest, " Run: ", run, " Time: ", time)
	print(total)
