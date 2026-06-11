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
    ope = int(input("enter a operator"))
    if ope == "add":
        add()
    elif ope == "subtract":
        subtract()
    elif ope == "multiply":
        multiply()
    elif ope == "divide":
        div()
        
except ValueError as e:
    print(e)
except SyntaxError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)