def add(x, y):
    return x+y
def minus(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    return x/y

num1 = float(input("Enter fist number: "))
num2 = float(input("Enter second number:"))

operation = input("Choose(+,-,*,/): ")

if operation == "+":
    print(add(num1,num2))
elif operation == "-":
    print(minus(num1,num2))
elif operation == "*":
    print(multi(num1, num2))
elif operation == "/":
    print(divide(num1, num2))
else:
    print("Invalid input")
    