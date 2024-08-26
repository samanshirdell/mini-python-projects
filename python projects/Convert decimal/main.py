# Program to Convert Decimal to Binary, Octal and Hexadecimal.
print("Welcome to the convert Decimal to Binary, Octal and Hexadecimal.")

number = int(input("Enter a number: "))

print(f"The decimal value of {number} is: ")
print(f"Binary: {bin(number)}")
print(f"Octal: {oct(number)}")
print(f"Hexadecimal: {hex(number)}")