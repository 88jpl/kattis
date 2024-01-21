n = int(input())
#print(bin(n))
theBin = bin(n)
reverse = ''
for i in range(1, len(bin(n))-1):
    reverse += theBin[(i*-1)]
answer = int(reverse, 2)
#print(reverse)
print(answer)
    
