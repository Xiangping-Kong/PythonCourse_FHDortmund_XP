# Read input string from user
s1 = input("Please enter a string: ")

# Collect all digits and convert to integers
digits = [int(char) for char in s1 if char.isdigit()]

# Calculate sum and average
total_sum = sum(digits)
if digits:
    average = total_sum / len(digits)
else:
    average = 0  # avoid division by zero when there are no digits

# Output results
print(f"Sum of digits: {total_sum}")
print(f"Average of digits: {average:.2f}")
