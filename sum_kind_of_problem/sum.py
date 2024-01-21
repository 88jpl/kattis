

def s1(n):
    list_positive = []
    for num in range(1, n + 1):
        list_positive.append(num)
        sums = sum(list_positive)
    return sums
    
    
def s2(n):
    list_nums = []
    for nums in range(1, n*2 + 1, 2):
        list_nums.append(nums)
        sums = sum(list_nums)
        
    return sums
    
    
def s3(n):
    list_nums = []
    for nums in range(2, n*2 + 1, 2):
        list_nums.append(nums)
        sums = sum(list_nums)
        
    return sums

N = int(input())
for i in range(N):
    items = input()
    list_items = items.split()
    theRange = list_items[1]
    sum_positive = 0
    answer = str(i+1) + " " + str(s1(int(theRange))) + " " + str(s2(int(theRange))) + " " + str(s3(int(theRange)))

    

    print(answer)

#    print()
#    print()