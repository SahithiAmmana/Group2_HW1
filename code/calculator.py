#Simple Calculctor

#Adds two numbers
def addition(a,b):
    return a+b

#Subtracts second number from the first
def subtraction(a,b):
    return a-b

#Multiplies two numbers
def multiplication(a,b):
    return a*b

#Divides first number by second
def division(a,b):
    if b==0:
        return "Enter non-zero divisor"
    else:
        return a/b


print(addition(3,4))
print(subtraction(4,5))
print(multiplication(10,8))
print(division(10,5))