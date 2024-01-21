pass1 = input()
pass2 = input()
digits = 0
power = 0 
for i in range(len(pass1)):
    if pass1[i] == pass2[i]:
        pass
    else:
        power += 1
        digits += 1
        #print(power, digits)
if digits == 0:
    print(1)
else:
    print(2 ** power)
