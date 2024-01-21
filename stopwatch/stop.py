n = int(input())
sum_list = []
if n % 2 == 1:
    print('still running')
else:

    for i in range(n):
        order = i+1
        
        if order % 2 == 1:
            last_start = int(input())
        else:
            total =  int(input()) - last_start
            sum_list.append(total)
    print(sum(sum_list))
