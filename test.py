def add(a , b):
    print(a + b)
def subtract(a , b):
    print(a - b)
def multiply(a , b):
    print(a * b)
def div(a , b):
    print(a / b)
try:
    print("Choose an operation")
    print("add , subtract, multiply, divide")
    ope = str(input("enter a operator"))
    print("enter value")
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    if ope == "add":
        add(a, b)
    elif ope == "subtract":
        subtract(a, b)
    elif ope == "multiply":
        multiply(a, b)
    elif ope == "divide":
        div(a, b)
        
except ValueError as e:
    print(e)
except SyntaxError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)