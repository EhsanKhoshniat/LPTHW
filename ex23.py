def dec2bin(decn):
	binn = 0
	power = 0
	while decn > 0 :
		binn += (decn % 2) * (10 ** power)
		decn //= 2
		power += 1
	return binn
	

x = int(raw_input("Enter the decimal number to convert it to binary: "))

print dec2bin(x)

