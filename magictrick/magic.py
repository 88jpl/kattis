line = input()
occurs = 1
for i in line:
    if line.count(i) > 1:
        occurs += 1
    else:
        continue

if occurs > 1:
    print(0)
else: 
    print(1)









