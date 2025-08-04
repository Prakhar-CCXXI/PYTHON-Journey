# Task 1: Read a File and Handle Errors

try:
    file1 = open('sample.txt', 'r')
    readfile1 = file1.readline()
    readfile2 = file1.readline()
    print("Reading file content:")
    print("Line 1:", readfile1)
    print("Line 2:", readfile2)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


# Task 2: Write and Append Data to a File


file2 = open('output.txt','w')
write = input('Enter text to write to the file :')
write_file = file2.write(write)
print("Data successfully written to output.txt.")
file2.close()

file2 = open('output.txt', 'a')
append = input('Enter additional text to :')
append_file = file2.write('\n'+append)
print("Data successfully append.")
file2.close()

file2 = open('output.txt', 'r')
read_file1 = file2.readline()
read_file2 = file2.readline()
print("Final content of output.txt:")
print(read_file1+'\n'+read_file2)

file2.close()



