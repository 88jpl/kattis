(n, k) = input().split()
count = 1
order = input().split()
for i in order:
	if count < 3 and int(i) == int(k):
		if count == 1:
			print("fyrst")
			break
		else:
			print("naestfyrst")
			break
	elif int(i) == int(k):
		print(count, "fyrst")
		break
	else:
		count += 1
