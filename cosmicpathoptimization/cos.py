s = input()
data = input().split()
data = [int(i) for i in data]
print(sum(data) // int(s))
