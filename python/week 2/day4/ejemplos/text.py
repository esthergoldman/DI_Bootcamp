blah = "blah.txt"

with open("blah.txt", "w") as f:
    f.write("hello\n")

with open("blah.txt", "a") as f:
    f.write("goodbye")

    # w write
    # r read
    # a append
    # w+ write + read
    # a+ append + read
