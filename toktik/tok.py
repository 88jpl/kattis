n = int(input())
accounts = {}
for i in range(n):
	txt = input().split()
	if accounts.get(txt[0]):
		accounts[txt[0]] += int(txt[1])
	else:
		accounts[txt[0]] = int(txt[1])
topScore = 0
topAccount = ""
for i in accounts:
	#print(i)
	if accounts[i] > topScore:
		topScore = accounts[i]
		topAccount = i
print(topAccount)
