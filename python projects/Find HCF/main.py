# Program to find H.C.F of two numbers.
print("Welcome to the find H.C.F of two input numbers.")

def find_hcf(x, y):
    if x > y:
        smaller = y
    elif y > x:
        smaller = x

    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

# Two input for function
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

# Print the result
print("The H.C.F is: ", find_hcf(num1, num2))
