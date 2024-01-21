n = int(input())
theMod = n % 100
theInt = n // 100

if theInt < 1:
	print('99')
elif theMod >= 49:
	#round up
	print( str(theInt) + str(99))
else:
	if theInt == 1:
		print('99')
	else:
	#round down if theInt not less then 1
		print( str(theInt - 1) + "99")
