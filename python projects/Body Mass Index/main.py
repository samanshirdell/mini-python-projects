# Program to calculate your Body Mass Index.
print("Welcome to the calculate your BMI")

def body_mass_index(height, weight):
    return round((weight / height**2), 2)

# height
ht = float(input("Enter your height in meters: "))
# weight
wt = float(input("Enter your weight in kg: "))

bmi = body_mass_index(ht, wt)
print(f"Your BMI is: {bmi}")

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese")