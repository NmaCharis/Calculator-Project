#Simple Calculator using functions
#to take 2 inputs
#its going to choose the operation to perform on the 2 inputs
#Results- To get the results and display it

#We first define the function and logic
def add(a , b):
    return a + b
def subtract(a , b):
    return a - b
def multiply(a , b):
    return a * b
def floordivision(a , b):
    return a // b
def exponent(a , b):
    return a ** b
def modulus(a , b):
    return a % b
def divide(a , b):
    if b == 0:
        return "error: can't be divided by zero"
    else:
        return a / b
#Writing the main calculator program
print("MY SIMPLE CALCULATOR")
print("choose operation:add, subtract, multiply and divide") 

#Now we write the input section
#first , ask the user to enter the first and second numbers to be converted to a float
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter the operation:").lower() # to ensure the operation is lowercase

#Next Step to write the code to perform the operation (if-else)
if operation == "add" :
    result = add(num1 , num2)
elif operation == "subtract":
    result = subtract(num1 , num2)
elif operation == "multiply":
    result = multiply(num1 , num2)
elif operation == "floordivision" :
    result = floordivision(num1 , num2)
elif operation == "exponent":
    result = exponent(num1 , num2)
elif operation == "modulus":
    result = modulus(num1 , num2)
elif operation == "divide":
    result = divide(num1 , num2)
else:
    result = "invalid operation, try again!!!!!"
print("RESULT:", result)

