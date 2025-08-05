#Task 1: Create a Dictionary of Student Marks

try:
    stud_dict = {'Ansh': '80', 'Yogi': '77', 'Azmat': '100', 'Alice': '85'}
    name = input("Enter the student's name:")
    print(stud_dict.get(name, 'Student not found.'))
except KeyError:
    print(name + "'s marks:" + stud_dict[name])


#Task 2: Demonstrate List Slicing

start=int(input("Enter the starting number:"))
end = int(input("Enter the ending number (add it by 1):"))
list = [i for i in range(start,end)]
extracted = list[0:5]
print("Your List is :",list)
print("Extracted first five elements:",extracted)
extracted.sort(reverse=True)
print("Reversed extracted elements:",extracted)

