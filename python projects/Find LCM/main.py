# Program to Find L.C.M of two input numbers.
print("Welcome to the find L.C.M of two numbers.")

def find_lcm(x, y):
    # Choose the greater number.
    if x > y:
        greater = x
    elif y > x:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

# Function inputs.
number_1 = int(input("Please enter a number: "))
number_2 = int(input("Please enter another number: "))

# Print result
print("THE L.C.M is: ", find_lcm(number_1, number_2))