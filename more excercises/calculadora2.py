num1 = float(input("enter a number:\n "))
op = input("enter a operator:\n ")
num2 = float(input("enter another number:\n "))

if op == "+":
    res = num1 + num2
    print("the result is: " + str(res))
elif op == "-":
    res= num1 - num2
    print("the result is: " + str(res))
elif op == "*":
    res = num1 * num2
    print("the result is: " + str(res))
elif op == "/":
    res = num1 / num2
    print("the result os: " + str(res))
else:
    print("oops try again")