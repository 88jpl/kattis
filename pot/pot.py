n = int(input())
num_list = []
for n in range(n):
    num = input()
    num_p = num[-1]
    num = num[:-1]
    answer = int(num) ** int(num_p)
    num_list.append(answer)
print(sum(num_list))
