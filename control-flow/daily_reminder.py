# Get pattern size from user
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw pattern using nested loops
while row < size:
    # Print asterisks for each column in the current row
    for col in range(size):
        print("*", end="")
    # Move to next line after completing each row
    print()
    row += 1











