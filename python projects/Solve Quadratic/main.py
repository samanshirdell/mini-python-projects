# Import math lib
import math

# Program to solve quadratic equation.
print("Welcome to the Solve Quadratic Equation.")

# Input coefficients
a = int(input("Please enter coefficients a: "))
b = int(input("Please enter coefficients b: "))
c = int(input("Please enter coefficients c: "))

# Calculate the discriminant
discriminant = b ** 2 - 4 * a * c # ==> Formula: b2 - 4ac

if discriminant > 0:
    # Two real distance answers
    answer_1 = -b + math.sqrt(discriminant) / (2 * a)
    answer_2 = -b - math.sqrt(discriminant) / (2 * a)
    # Print Answers
    print(f"Answer1: {answer_1}")
    print(f"Answer2: {answer_2}")

elif discriminant == 0:
    # One real answer
    answer = -b / (2 * a)
    # Print answer
    print(f"Answer: {answer}")

else:
    # Complex answer
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    # Print real_part and imaginary_part
    print(f"Answer1: {real_part} + {imaginary_part}i")
    print(f"Answer2: {real_part} - {imaginary_part}i")