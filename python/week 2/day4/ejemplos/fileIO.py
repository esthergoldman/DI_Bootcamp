with open("blah.txt", "w") as f:
	f.write("Hello\n")
with open("blah.txt", "a") as f:
	f.write("Goodbye")
with open("blah.txt", "r") as f:
	data = f.readlines()
# w  write
# r  read
# a  append
# w+ write + read
# a+ append + read
# Reading..
# f.read()		Reads the entire file into a single string
# f.readline()	Reads a single line
# f.readlines() Reads the entire file into a list of strings