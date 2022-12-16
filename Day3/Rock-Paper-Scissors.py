import random

def who_wins(user_input, comp_input, user_score, comp_score):

    if user_input == "R":

        if comp_input == "S":
            print("-----------------------------")
            print("User Won!!\n")
            print("-----------------------------")
            user_score+=1

        elif comp_input == "P":
            print("-----------------------------")
            print("Computer Won!!!\n")
            print("-----------------------------")
            comp_score+=1
        
        else:
            print("-----------------------------")
            print("Draw")
            print("-----------------------------")

    elif user_input == "P":

        if comp_input == "R":
            print("-----------------------------")
            print("User Won!!!\n")
            print("-----------------------------")
            user_score+=1

        elif comp_input == "S":
            print("-----------------------------")
            print("Computer Won!!!\n")
            print("-----------------------------")
            comp_score+=1
        
        else:
            print("-----------------------------")
            print("Draw")
            print("-----------------------------")

    elif user_input == "S":

        if comp_input == "P":
            print("-----------------------------")
            print("User Won!!!\n")
            print("-----------------------------")
            user_score+=1

        elif comp_input == "R":
            print("-----------------------------")
            print("Computer Won!!!\n")
            print("-----------------------------")
            comp_score+=1
        
        else:
            print("-----------------------------")
    
    else:
        print("-----------------------------")
        print("INVALID INPUT\n")
        print("-----------------------------")





comp_score = 0
user_score = 0
continu = "Y"
comp_choice_list = ["R", "P", "S"]
while continu == "Y":
    
    user_input = input("\nEnter you choice among [R/P/S] : ")
    comp_input = random.choice(comp_choice_list)
    print("\nUser Choice : " + user_input + " | Computer Choice : " + comp_input)
    who_wins(user_input, comp_input, user_score, comp_score) 
    continu = input("Do you want to continue playing [Y/N] : ")

print("-----------------------------")
print("User Score : " + user_score + "\nComputer Score: " + comp_score)
if user_score > comp_score:
	print("In Grand total, User Won!!")
elif user_score < comp_score:
	print("In Grand total, Computer Won!!")
else:
	print("In Grand total, Match was a Draw")
print("Thanks for Playing!!!\nCome Again Tommorrow")
print("-----------------------------")
