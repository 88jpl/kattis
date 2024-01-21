n = int(input())
for n in range(n):
    data = input()
    data = data.split(' ')
    first = int(data[0])
    
    display = []
    for fir in range(first):
        above_avg = []
        dataB = data[1:]
        int_list = list(map(int, dataB))
        total = sum(int_list)
        avg = total / first
        #print(fir)
        
        if int_list[fir] > avg:
            
            above_avg.append(fir)
        else:
            continue
        answer = avg /len(above_avg)
        print(answer)
        display.append('%.3f'%answer + '%\n')
        
print(display)

