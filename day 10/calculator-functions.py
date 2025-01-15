def add(a, b):
    addt = a + b
    return addt

def subtraction(a, b):
    subt = a - b
    return subt

def multiplication(a, b):
    mult = a * b
    return mult

def division(a, b):
    divs = a / b
    return divs

num1 = int(input("What's the first number? \n"))
print('+ \n-\n*\n/')
operation = input("Pick an operation!\n")
num2 = int(input("Please pick a second number!\n"))

if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtraction(num1, num2))
elif operation == '*':
    print(multiplication(num1, num2))
elif operation == '/':
    print(division(num1, num2))
else:
    print('Please pick a valid operation.')
    
