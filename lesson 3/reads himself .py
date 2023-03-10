import sys
filename = sys.argv[0]
file = open(filename, 'r')
for line in file:
	print(line, end="")
file.close()
