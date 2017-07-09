# i = 0
# numbers = []

# while i < 6:
# 	print "At te top i is %d" % i
# 	numbers.append(i)

# 	i += 1
# 	print "Numbers now: ", numbers
# 	print "At the bottum i is %d" % i


# print "The numbers: "

# for num in numbers:
# 	print num

# def printnum(n, x):
# 	i = 0
# 	numbers = []
# 	while i < n:
# 		numbers.append(i)
# 		i += x
# 	for num in numbers:
# 		print num

# printnum(6, 2)

def printnum(n, x):
	i = 0
	numbers = []
	for i in range(0, n, x):
		numbers.append(i)
		i += 1
	for num in numbers:
		print num

printnum(6, 2)