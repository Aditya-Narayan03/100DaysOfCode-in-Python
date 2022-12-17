import random


difficulty_level = input("Set difficulty level [Easy/Medium/Hard] : ").lower().strip()
if difficulty_level == "easy":
    print("OKAY!!! You chose " + difficulty_level.capitalize() + " level.\nGood for you 😏")

elif difficulty_level == "medium":
    print("OKAY!!! You chose " + difficulty_level.capitalize() + " level.\nOhhhh You want to challenge me")

elif difficulty_level == "hard":
    print("OKAY!!! You chose " + difficulty_level.capitalize() + " level.\nMove Ahead at your own risk")

else:
    print("Please enter difficutly level using the given option.\nQuitting Game.")
    quit()

def check_validity(value):
    if value.isdigit():
        value = int(value)
        return value

        if value <= 0:
            print("Please enter range larger than 0\nQuitting the game.")
            quit()
    
    else:
        print("Please enter a valid digit.\nQuitting the game.")
        quit()


user_range = input("Enter the range for the game : ")
check_validity(user_range)
random_value = random.randint(1, int(user_range))

continu = "Y"
while continu == "Y":
    user_guess = input("Enter your guess : ")
    check_validity(user_guess)
    # calc = int(user_range) - int(user_guess)
    if int(user_guess) == random_value:
        print("\nYou're guess is correct. Congrats!!!")
        print("Thanks for playing!!!")
        quit()
    
    elif int(user_guess) > random_value:
        print("Your guess is larger than the random number.\nTry going for something smaller.")
    
    elif int(user_guess) < random_value:
        print("Your guess is smaller than the random number.\nTry going for something larger.")
    


    
    
    continu = input("Do you want to contiue playing [Y/N] : ")
    if continu != "Y":
        print("\nThanks for Playing!!!!")
        quit()