print("Welcome to the calculator!")

operator = input("Choose your arithmetic(+, -, *, /):")


try:
    num1 = int(input("Write a number"))
    
except:
    print("You have to write a number")
    num1 = 0

try:
    num2 = int(input("Write a number"))
    
except:
    print("You have to write a number")
    num2 = 0

if operator == "+":
    sum = num1 + num2
elif operator == "-":
    sum = num1 - num2
elif operator == "*":
    sum = num1 * num2
elif operator == "/":
    sum = num1 / num2


else:
    print("Fail")

print("the sum is:", sum)

