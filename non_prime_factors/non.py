import sympy
n = int(input())
answers = []
check = []
for i in range(n):
    num = int(input())
    check.append(num)
for i in check:
    factors = []
    primes = 0
    for ii in range(1, i+1):
        if i % ii == 0:
            factors.append(ii)
        else:
            pass
    for iii in factors:
        if sympy.isprime(iii) == True:
            primes += 1
        else:
            pass
    
    answers.append(len(factors)-primes)
#print(factors)
print(*answers, sep = '\n')
