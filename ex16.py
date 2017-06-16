from sys import argv

script, filename = argv #define command-line arguments

print "We're going to erase %r." % filename #tells something about the file defined by command-line
print "If you don't whant that, hit CTRL-C (^C)."
print "If you do whant that, hit RETURN."

raw_input("?")	#CTRL-C interrupts the command-line

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

final_txt = line1 + "\n" + line2 + "\n" + line3
target.write(final_txt)
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")



print "And finally, we close it."
target.close()

new_file = open(filename)
print "Here is the new file: "
print new_file.read()