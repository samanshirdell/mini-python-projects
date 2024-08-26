print("Welcome to the Tresure Island")
print("Your mission is to find the Tresure")

while True:
    step_1 = input("You're at a cross road. Where you want to go: Type \"Left\" or \"Right\": ").lower()
    if step_1 == "right":
        print("All Right.")
        step_2 = input("You come to lake. There is an island in the middle of the lake. Type \"Wait\" or \"Swim\": ").lower()
        if step_2 == "wait":
            print("Good Job.")
            step_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One Red, One Yellow, One Blue. Which colour do you chooses: ").lower()
            if step_3 == "blue":
                print("YOU WIN!!!")
                again = input("Do you want to play again: Type 'Yes' or 'No': ").lower()
                if again == "yes":
                    print("Okay, Let's to this.")
                    continue
                elif again == "no":
                    print("Thanks for playing...")
                    break
            elif step_3 == "red":
                print("YOU LOSE!")
                break
            elif step_3 == "yellow":
                print("YOU LOSE!")
                break
            else:
                print("Please type Yellow, Red or Blue.")
        elif step_2 == "swim":
            break
        else:
            print("Please type Swim or Wait.")
            continue
    elif step_1 == "left":
        print("YOU LOSE!")
        break
    else:
        print("Please type Left or Right.")
        continue