# ask the user for their name if the name begins with the 
# letter a print a if b print b if c print c if none 
# of the above print does not start with a b or c

name = input('name please\n')
name2 = name.lower()

if name2.startswith('a'):
    print('a')
elif name2.startswith('b'):
    print('b')
elif name2.startswith('c'):
    print('c')
else:
    print ("name must start with a,b or c")
 




