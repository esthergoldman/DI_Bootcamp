askuser = input("give me a string ")
askuser_length = len(askuser) #expression

if askuser_length>=10:
	print("string ok")     #true expression value

else:
	print("string short") #not=keyword long=integer

print(askuser[0])



for number in range(0,askuser_length+1):
	print(askuser[0:number])




#import random

#number = askuser_length
#random.shuffle(number)
#print("List after first shuffle:", number)






#a ="hello,world!"
#print(a[1]) prints e


#this_string = "Hey I am CodeSpeedy"
#for character_index in this_string:
 #  print(character_index) # print each character at a time from string


