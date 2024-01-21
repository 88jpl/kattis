n = input()
record = 0 
for l in n:
    if l == 'a':
        print(n[record:])
        break
    else:
        record += 1
        #print(record)
