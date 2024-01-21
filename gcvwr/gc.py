weights = input().split()
weights = list(map(int, weights))
gcvwr = weights[0]
truck = weights[1]
items = input().split()
items = list(map(int, items))
sumItems = sum(items)
print(round(((gcvwr-truck)*.9)-sumItems))

