txt = input()
t = txt.count("T")
c = txt.count("C")
g = txt.count("G")
aList = [t,c,g]
#print(min(aList))
print((t ** 2) + (c ** 2) + (g ** 2) + ((min(aList)) * 7))
