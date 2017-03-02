numb = int(input("Inser a number: "))
sum = 0

while numb != 0 :
	print(numb % 10, end = '')
	
	sum += numb % 10
	numb //= 10
	
	if numb != 0:
		print(" + ", end = '')
	
print(' =', sum)
