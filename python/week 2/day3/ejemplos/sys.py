import sys
if __name__ == "__main__":
# if this file was loaded from the terminal
	total = 0
	for num in sys.argv[1:]:
		total += int(num)
	print(total)