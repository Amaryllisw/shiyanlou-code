count = 0
for num in range(1, 101):
	if num == 7 or num % 10 == 7 or num // 10 == 7:
		num += 1
		count += 1
		continue
	print(num)
print("total pass {} time".format(count))
		
