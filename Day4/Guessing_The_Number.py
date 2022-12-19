import random

print("-------------------------------------")
difficulty_level = input("Set difficulty level [Easy/Medium/Hard] : ").lower().strip()
if difficulty_level == "easy":
    num_guesses = 10
    print("OKAY!!! You chose " + difficulty_level.capitalize() + " level.\nYou'll get 10 guesses to make. Good for you 😏")

elif difficulty_level == "medium":
    num_guesses = 5
    print("OKAY!!! You chose " + difficulty_level.capitalize() + " level.\nYou'll get 5 guesses to make. Beware...it can be challenging")

elif difficulty_level == "hard":
    num_guesses = 3
    print("OKAY!!! You chose " + difficulty_level.capitalize() + " level.\nYou'll get 3 guesses to make. Move Ahead at your own risk")

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

print("-------------------------------------")
user_range = input("Enter the range for the game : ")
check_validity(user_range)
random_value = random.randint(1, int(user_range))

guesses_made = 1
continu = "Y"
while num_guesses > 0:
    print("-------------------------------------")
    user_guess = input(f"\nEnter your guess number {guesses_made} : ")
    print("-------------------------------------")
    check_validity(user_guess)
    guesses_made += 1
    if int(user_guess) == random_value:
        print("-------------------------------------")
        print("\nYou're guess is correct. Congrats!!!")
        print("Thanks for playing!!!")
        quit()
    
    elif int(user_guess) > random_value:
        num_guesses = num_guesses - 1
        if num_guesses <= 0:
            print("-------------------------------------")
            print("\nThat is incorrect answer!!!\nAnd \
also you ran out of Guesses.....Better luck next time. ")

            break
        print("-------------------------------------")
        print("Your guess is larger than the random number.\nTry going for something smaller.")
        print(f"You only have {num_guesses} guesses left.")
        print("-------------------------------------")
    
    elif int(user_guess) < random_value:
        num_guesses = num_guesses - 1
        if num_guesses <= 0:
            print("-------------------------------------")
            print("\nThat is incorrect answer!!!\nAnd \
also you ran out of Guesses.....Better luck next time. ")

            break
        print("-------------------------------------")
        print("\nYour guess is smaller than the random number.\nTry going for something larger.")
        print(f"You only have {num_guesses} guesses left.")
        print("-------------------------------------")
