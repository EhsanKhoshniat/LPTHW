from sys import argv

script, first, second, third = argv

print "The script is called:", script #argv 0
print "Your first variable is:", first #argv 1 and so on 
print "Your second variable is:", second
print "Your third variable is:", third

yes_or_no = raw_input("Did you get it? ")

print "hmm, %s" % yes_or_no