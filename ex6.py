x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y

print "I said: %r." % x # %r is used for debugging since it displays the "raw" data of the variable.
print "I also said: %s." % y # use %s and others for displaying to users.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #No need to define format in same line. BTW I find it funny.

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e