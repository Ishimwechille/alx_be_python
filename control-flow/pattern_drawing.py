# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# While loop to control the number of rows
while row < size:
    # For loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print without a newline
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
