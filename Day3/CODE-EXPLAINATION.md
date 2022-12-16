# TASK EXPLAINATION : 

## **Rock Paper Scissors**

You may have played rock paper scissors before. Maybe you’ve used it to decide who pays for dinner or who gets first choice of players for a team.

If you’re unfamiliar, rock paper scissors is a hand game for two or more players. Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock (a fist), a piece of paper (palm facing downward), or a pair of scissors (two fingers extended). The rules are straightforward:

    Rock smashes scissors.
    Paper covers rock.
    Scissors cut paper

# PROGRAM EXPLAINATION :

Let me explain how we are going to make it.

- First we'll take the user input and store it in a variable.
- Then we want to take compter's input and for that we'll generate a random value from a list that will contain 3 values i.e. Rock, Paper and Scissors.
- After that we will call a function to decide who won based on both of those inputs.
- This function will contain 3 if-else statement that will check for the user input.
- Inside each of those 3 if-statements we will write 2 more if-statements that will check for the computer's inputs.
- Inside these nested if statements we will have variables that will count the score for user and computer & increment themselves.
- Also remember the game has to run until the user wants to continue, so everything will be inside a while loop that will run infinitely until the user chooses to quit.
- Upon quiting the screen will display the score of user and computer and also along with that a message for > Thanks for Playing!!


# CODE EXPLAINATION :

- First we will import _random_ module because we need to generate random values in our program.
- After that we will define 2 variables **user_input** & **comp_input**. And set their intial value to 0.
- Now we need to define a variable that will prompt user whether to continue the game or quit.
- We also need to define a list that will act as computer's input. This list will have 3 values i.e. _Rock, Paper, Scissors_.
- From here we will start our while loop and this while loop will run infintely until user specifies to quit.
- Inside this loop we will take user input and generate random value using random module with the list that we created earlier.
- We will now call the function to decide the winner for the game based on the score of user and computer.

###### Now explaination of function:

- We will pass 4 arguments onto this function : _"user_input", "comp_input", "user_score", "comp_score".
- We will define the 1st if and put a condition to check whether the value of *user_input* is equal to "R".
- Inside this we will define a nested loop that will check if *comp_input* is equal to "S", and if the condition is **True**, then *user_score* will increment.
- If the condiion is false, for that we will define an elif that will check if the *comp_input* is equal to "P", and if the condition is **True**, then *comp_score* will increment.
- In the case where all of these conditions fail to satisfy, we have to define an else for that, and it will just print > DRAW
- We will do this same procedure for all other values of *user_input* and then define nested if-else for all other values of *comp_input*.
- The scores will be counted and in the end of the program, when the user decides to quit, we will print the grand-total of both the scores.
- The grand-total will then be compared and the winner will be decided. With this line of code we will end our game. 
