mylist = [2,3,1,"four",2,42,1,5,3,None]
def make_sum(mylist):
	total = 0
	for num in mylist:
		try:
			total += num
		except TypeError:
			continue
	return total
total = make_sum(mylist)
print(total)


# Using exception  handling to add numbers in a list, even when the list contains garbage information: