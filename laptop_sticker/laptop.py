n = input().split()
wc = int(n[0])
hc = int(n[1])
ws = int(n[2])
hs = int(n[3])
if wc - ws >= 2:
    if hc - hs >= 2:
        print(1)
    else:
        print(0)
else:
    print(0)
