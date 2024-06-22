(n, m) = input().split()
n = int(n)
m = int(m)
diff = n - m
if diff == 1:
	print(f"Dr. Chaz needs 1 more piece of chicken!")
elif diff == -1:
	print(f"Dr. Chaz will have 1 piece of chicken left over!")
elif diff > 0:
	print(f"Dr. Chaz needs {diff} more pieces of chicken!")
else:
	print(f"Dr. Chaz will have {abs(diff)} pieces of chicken left over!")
