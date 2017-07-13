from sys import argv 

script , filename = argv #define command line arguments

txt = open(filename)	#opens file defined by command-line

print "Here's your file %r:" % filename 	#prints the opened file's name
print txt.readlines()	#reads the file's content

print "Type the filename again:"	
file_again = raw_input("> ")	#open file in another way, with raw_input method 

with open(file_again) as txt_again:  # "with" statement 
	print txt_again.read()

# txt_again = open(file_agian)	#opens file defined by raw_input

# print txt_again.read()			#read the file

txt_again.close()