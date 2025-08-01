# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

add = a + b
sub = a - b
mul = a*b
div = a/b

print("Addition: " ,add)
print("Subtraction: " ,sub)
print("Multiplication: " ,mul)
print("Division: " ,div)


# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

firstname = input("Enter your first name: ")
lastname = input("Enter your last: ")

print("Hello, " + firstname +" "+ lastname + "! Welcome to the Python program")
