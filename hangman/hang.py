word = input()
guess = input()
count = 0
i = 0
while count < 10:
	if len(word) == 0:
		print("WIN")
		break
	else:
		oldLength = len(word)
		word = word.replace(guess[i], "")
		#print(word, guess[i])
		if oldLength == len(word):
			count += 1
	i += 1
			
if len(word) > 0:
	print("LOSE")
