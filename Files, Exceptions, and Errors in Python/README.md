# Assignment 4 : File Handling Tasks in Python

This project contains two main tasks demonstrating basic file operations in Python, including reading files with error handling, and writing/appending data to a file.

## Task 1: Read a File and Handle Errors

- The program attempts to open and read the first two lines from a file named `sample.txt`.
- It prints the contents of these lines to the console.
- If the file does not exist, the program handles the `FileNotFoundError` exception gracefully by printing an error message.
- The file is properly closed after reading.

## Task 2: Write and Append Data to a File

- The program prompts the user to input text which is written to a new file called `output.txt` (overwriting any existing content).
- It then asks the user to input additional text, which is appended to `output.txt` starting on a new line.
- The program opens `output.txt` again for reading and reads the first two lines.
- Finally, it prints these two lines from the file to show the combined content that was written and appended.
- All files are closed properly after operations.

This code provides a simple example of file input/output (I/O), user interaction, and basic error handling in Python.
