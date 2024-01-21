length = int(input())
text = input()
numbers = []
num = ""
previous = False
for i in text:
	if previous and (not i.isdigit()):
		numbers.append(num)
		num = ""
		#print("erase num")
	if i.isdigit():
		previous = True
		num += i
	else:
		previous = False
if len(num) > 0:
	numbers.append(num)
intNumbers = []
for n in numbers:
	intNumbers.append(int(n))
print(max(intNumbers))
