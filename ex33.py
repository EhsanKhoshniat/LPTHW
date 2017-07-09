i = 0
numbers = []

while i < 6:
	print "At te top i is %d" % i
	numbers.append(i)

	i += 1
	print "Numbers now: ", numbers
	print "At the bottum i is %d" % i


print "The numbers: "

for num in numbers:
	print num

