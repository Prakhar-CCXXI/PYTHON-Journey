
# Task 1: Calculate Factorial Using a Function
n = int(input("Enter a number:"))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n*(factorial(n-1))



print("Factorial of",n,"is:",factorial(n))

# Task 2: Using the Math Module for Calculations

import math

m = int(input("Enter a number:"))

sqr =  math.sqrt(m)
log = math.log(m)
sine_value = math.sin(m)

print("Square root:",sqr)
print("Logarithm:",log)
print("Sine:",sine_value)

