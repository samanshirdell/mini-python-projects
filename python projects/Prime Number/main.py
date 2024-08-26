# Program to Check Prime Number.
print("Welcome to the check Prime Number.")

number = int(input("Enter a number: "))

# Define status variable.
status = False

if number == 1:
    print(f"{number}, Is not prime number.")

elif number > 1:
    for i in range(2, number):
        if number % i == 0:
            status = True
            break

if status:
    print(f"{number}, Is not prime number.")

else:
    print(f"{number}, Is prime number.")