n = int(input())
remaining = n
layer = 0
for i in range(1,100000 ,2):
    build = i**2
    if remaining - build >= 0:
        layer += 1
        remaining -=  build
#        print(remaining)
    else:
        print(layer)
        break
