n = input().split()
a = n[0]
b = n[1]
backA = a[::-1]
backB = b[::-1]
if backA > backB:
    print(backA)
else:
    print(backB)
