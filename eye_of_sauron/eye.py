fort = input()
fort2 = fort.strip('()')
fort3 = fort.split('()')
if len(fort2) % 2 == 1:
    print("fix")
else: 
    if len(fort3[1]) == len(fort3[0]):
        print("correct")
    else:
        print('fix')
#print(fort3)
#print(len(fort3[1]))
#print(len(fort3[0]))
