n = input()
countSmile = 0
countFrowny = 0
if ":)" in n and ":(" in n:
	print("double agent")
elif ":)" in n:
	print("alive")
elif ":(" in n:
	print("undead")
else:
	print("machine")
