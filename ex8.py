formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing", #I forgot the "," and got "not enough arguments for format string" error.
	"That you could type up right.", 
	"But it didn't sing", #It prints this with double-quotes and others with single-quotes, because of "didn't".
	"So I said goodnight."
	)
