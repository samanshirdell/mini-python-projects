import random
print("Welcome to Password Generator.")

def main():
    while True:
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '+']

        nr_letter = int(input("How many letter would you like in your password: "))
        nr_number = int(input("How many numbers would you like in your password: "))
        nr_symbol = int(input("How many symbol would you like in your password: "))

        password_list = []
        for char in range(nr_letter + 1):
            password_list.append(random.choice(alphabet))

        for char in range(nr_number + 1):
            password_list.append(random.choice(numbers))

        for char in range(nr_symbol + 1):
            password_list.append(random.choice(symbols))

        # shuffle the password list. e.g ["a", "b", "C"] ---> ["C", "b", "a"]
        random.shuffle(password_list)

        password = ""
        for items in password_list:
            password += items
        print(f"Your password is: {password}")

        while True:
            again = input("Do you want to try again: Type 'Yes' or 'No': ").lower()
            if again == "yes":
                print("All Right")
                return main()
            elif again == "no":
                print("Thanks for visiting")
                return
            else:
                print("Please type Yes or No.")
                continue

if __name__ == '__main__':
    main()