n = input()
nums = []
for i in range(int(n), 1000000000):
    nums = []
    for number in str(i):
        nums.append(int(number))
        sums = sum(nums)
        print(sums)
        print(nums)
        if int(i) % sums == 0:
            print(i)
            break
        else:
            continue

    
