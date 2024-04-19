# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate maximum
maximum = max(num1, num2, num3)

# Calculate minimum
minimum = min(num1, num2, num3)

# Calculate total
total = num1 + num2 + num3

# Calculate average
average = total / 3

# Print results
print("Maximum is:", maximum)
print("Minimum is:", minimum)
print("Total: is", total)
print("Average: is", average)
