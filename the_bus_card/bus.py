import math

n = int(input())
time  = 0
n = int(math.ceil(n / 100.0)) * 100
if n / 500 >= 1.0:
	many = n // 500
	n -= many * 500
	time += many
if n / 200 >= 1.0:
	many = n // 200
	n -= many * 200
	time += many
if n / 100 >= 1.0:
	many = n // 100
	n -= many * 100
	time += many

print(time )
