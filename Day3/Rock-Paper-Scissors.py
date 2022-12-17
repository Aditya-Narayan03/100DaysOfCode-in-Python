import random


# def who_wins(user_input, comp_input):

#     if user_input == "R":

#         if comp_input == "S":
#             print("-----------------------------")
#             print("User Won!!\n")
#             print("-----------------------------")
           
#             user_score = user_score + 1
             
#             return user_score

#         elif comp_input == "P":
#             print("-----------------------------")
#             print("Computer Won!!!\n")
#             print("-----------------------------")
            
#             comp_score = comp_score + 1
               
#             return comp_score

#         else:
#             print("-----------------------------")
#             print("Draw")
#             print("-----------------------------")

#     elif user_input == "P":

#         if comp_input == "R":
#             print("-----------------------------")
#             print("User Won!!!\n")
#             print("-----------------------------")
            
#             user_score = user_score + 1
             
#             return user_score

#         elif comp_input == "S":
#             print("-----------------------------")
#             print("Computer Won!!!\n")
#             print("-----------------------------")
#             comp_score = comp_score + 1
               
#             return comp_score

#         else:
#             print("-----------------------------")
#             print("Draw")
#             print("-----------------------------")

#     elif user_input == "S":

#         if comp_input == "P":
#             print("-----------------------------")
#             print("User Won!!!\n")
#             print("-----------------------------")
            
#             user_score = user_score + 1
             
#             return user_score

#         elif comp_input == "R":
#             print("-----------------------------")
#             print("Computer Won!!!\n")
#             print("-----------------------------")
            
#             comp_score = comp_score + 1
               
#             return comp_score
        
#         else:
#             print("-----------------------------")
#             print("Draw")
#             print("-----------------------------")
    
#     else:
#         print("-----------------------------")
#         print("INVALID INPUT\n")
#         print("-----------------------------")




global comp_score
comp_score = 0
global user_score
user_score = 0
continu = "Y"
comp_choice_list = ["R", "P", "S"]
while continu == "Y":
    
    print("-----------------------------------------------")
    user_input = input("\nEnter you choice among [R/P/S] : ").upper().strip()
    comp_input = random.choice(comp_choice_list)
    print("\nUser Choice : " + user_input + "    |     Computer Choice : " + comp_input)
    if user_input == "R":

        if comp_input == "S":
            print("------------")
            print("| User Won |")
            print("------------")
           
            user_score = user_score + 1
             
            

        elif comp_input == "P":
            print("----------------")
            print("| Computer Won |")   
            print("----------------")
            
            comp_score = comp_score + 1
               
      

        else:
            print("--------")
            print("| DRAW |")
            print("--------")


    elif user_input == "P":

        if comp_input == "R":
            print("------------")
            print("| User Won |")
            print("------------")
            
            user_score = user_score + 1
             
           

        elif comp_input == "S":
            print("----------------")
            print("| Computer Won |")   
            print("----------------")
            comp_score = comp_score + 1
               
            

        else:
            print("--------")
            print("| DRAW |")
            print("--------")

    elif user_input == "S":

        if comp_input == "P":
            print("------------")
            print("| User Won |")
            print("------------")
            
            user_score = user_score + 1
             
           

        elif comp_input == "R":
            print("----------------")
            print("| Computer Won |")   
            print("----------------")
            
            comp_score = comp_score + 1
               
           
        
        else:
            print("--------")
            print("| DRAW |")
            print("--------")
    
    else:
        print("--------------------")
        print("| INVALID ARGUMENT |\n")
        print("--------------------")

    print("\n-----------------------------------------------")    
    continu = input("\nDo you want to continue playing [Y/N] : ")



print("-----------------------------------------------")
print("\nUser Score : ", user_score, sep=" ")
print("Computer Score: ", comp_score, sep=" ")

if user_score > comp_score:
	print("In Grand total, User Won!!")
elif user_score < comp_score:
	print("In Grand total, Computer Won!!")
else:
	print("In Grand total, Match was a Draw")

print("Thanks for Playing!!!\nCome Again Tommorrow")
print("-----------------------------------------------")
