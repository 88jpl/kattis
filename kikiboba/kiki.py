txt = input()
b = txt.count("b")
k = txt.count("k")
if b > k:
	print("boba")
elif k > b:
	print("kiki")
elif k == b and k != 0:
	print("boki")
else:
	print("none")
