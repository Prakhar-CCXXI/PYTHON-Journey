#   Assignment 6 - CALCULATOR USING TKINTER

This is a simple calculator application built using Python's Tkinter library. It supports basic arithmetic operations (addition, subtraction, multiplication, division), number input (including '00'), and result evaluation.

---

## Features

- User-Friendly GUI using Tkinter
- Supports addition, subtraction, multiplication, and division
- Buttons for digits 0-9 and '00'
- Entry field displays current input/result
- CLEAR button to reset entry field

---

## Usage

1. **Launch the Program:**  
   Run the script using Python (Python 3 recommended).

2. **Input Numbers:**  
   Click numeric buttons to enter numbers. To enter '00' at once, use the '00' button.

3. **Choose Operation:**  
   Click an operator button (+, -, x, /) to select the operation. Enter the next number.

4. **Get Result:**  
   Press '=' to evaluate and display the result.

5. **Clear Entry:**  
   Click the CLEAR button to reset the entry box.

---

## How It Works

- **Entry Widget:**  
  Displays numbers as you input them and shows results after calculations.

- **Button Functions:**
  - Number/‘00’ buttons append their value to the entry.
  - Operator buttons save the current value and operation.
  - '=' gets the second value, performs the pending operation, and displays the result.
  - CLEAR erases all input.

---

## File Structure

- **calculator.py**  
  The main Python script with all functionalities and GUI definitions.

---

## Requirements

- Python 3.x
- Tkinter (usually included with Python installation)

---

## Example

