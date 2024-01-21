n = int(input())
receipts = input().split()
receipts = list(map(int, receipts))
expenses = []
for i in receipts:
    if i < 0:
        expenses.append(i)
    else:
        continue
print(abs(sum(expenses)))
