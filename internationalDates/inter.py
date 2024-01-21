theInput = input()
i = theInput.split('/')
#print(i[0],i[1])
if int(i[0]) > 12:
	print('EU')
else:
	if int(i[1]) <= 12:	
		print('either')
	else:
		print('US')
