n = input().split()
a = int(n[0])
b = int(n[1])
if a + b == 0:
    print('Not a moose')
elif a == b:
    print('Even', a+b)
else:
    if a > b:
        print('Odd', a*2)
    else:
        print('Odd', b*2)
