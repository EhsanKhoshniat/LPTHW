from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()	#well, reads the file

def rewind(f):
	f.seek(0)	# A seek() operation moves pointer to some other part of the file,
	# so you can read or write at that place

def print_a_line(line_count, f):
	print line_count, f.readline() #prints line's count and a line of file

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file) #move pointer to the the beginning of the file

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)