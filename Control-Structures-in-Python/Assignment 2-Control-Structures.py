# Task 1: Check if a Number is Even or Odd

n = int(input("Enter a number: "))

if(n%2==0):
    print(n,"is an even number.")
else:
    print(n,"is an odd number.")


#Task 2: Sum of Integers from 1 to 50 Using a Loop

sum = 0
for i in range(1,51):
    sum += i
print("The sum of numbers from 1 to 50 is :",sum)
