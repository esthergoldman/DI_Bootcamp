# # Exercise 4 : How Many Characters In A Sentence ?

# my_text = " Sit Lorem consequat nulla ad sit. Occaecat exercitation deserunt laborum ullamco sunt ullamco non elit mollit irure. Deserunt sit dolore pariatur eiusmod ipsum. Irure proident laboris esse et incididunt dolor. Irure sit sint irure incididunt est voluptate incididunt sint dolor irure ut. Do adipisicing amet deserunt nisi reprehenderit aute veniam dolor cillum magna esse Lorem. Magna pariatur magna fugiat non nisi fugiat adipisicing incididunt reprehenderit duis cupidatat."


# print(len(my_text))


# ex 2
# Keep asking the user to input the longest sentence they can without the character “A” in it
# Each time a user successfully sets the new longest sentence print a congratulations message

while True:
    ask_user = input(
        "longest sentence you can write without the character “A” in it\n")
    if not ask_user.find("a") == -1:
        print("oops try again")
        continue
    else:
        print("congratulations")
        break


# while True:
#     data = input("Please enter a loud message (must be all caps): ")
#     if not data.isupper():
#         print("Sorry, your response was not loud enough.")
#         continue
#     else:
#         # we're happy with the value given.
#         # we're ready to exit the loop.
#         break

# while True:
#     data = input("Pick an answer from A to D:")
#     if data.lower() not in ('a', 'b', 'c', 'd'):
#         print("Not an appropriate choice.")
#     else:
#         break
