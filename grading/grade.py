n = input().split()
n = list(map(int, n))
a = n[0]
b = n[1]
c = n[2]
d = n[3]
e = n[4]
score = int(input())

if score < e:
    print('F')
elif score < d:
    print('E')
elif score < c:
    print('D')
elif score < b:
    print('C')
elif score < a:
    print('B')
else:
    print('A')
