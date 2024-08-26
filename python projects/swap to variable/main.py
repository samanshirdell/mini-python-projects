# A program to swap two variables.
print("Welcome to swap to variables program.")

# Input two variables.
number_1 = int(input("Enter the value of the first variable: "))
number_2 = int(input("Enter the value of the second variable: "))

# Display numbers.
print(f"first number is: {number_1} and second number is: {number_2}")

# Swap the values
temp = number_1
number_1 = number_2
number_2 = temp

# NOTE: Swapping without a temporary variable: ---> a = 3, b = 4 ==> a, b = b, a
# a = 3
# b = 4
# ==> a, b = b, a ==> a = 4, b = 3

# Display the swapped values.
print(f"Swapped values --> first number:{number_1}, second number: {number_2}")