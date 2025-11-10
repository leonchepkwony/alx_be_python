# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 1

# Use a while loop for rows
while row <= size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisks side by side
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
