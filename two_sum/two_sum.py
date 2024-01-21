import sys
for line in sys.stdin:
    ints = line.split()
    map_object = map(int, ints)
    list_of_ints = list(map_object)
    
    
    print(sum(list_of_ints))
    
