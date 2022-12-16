Task Explaination: 

Like the title suggests, this project involves writing a program that simulates rolling dice. 
- When the program runs, it will randomly choose a number between 1 and 6.
- The program will print what that number is. 
- It should then ask you if you’d like to roll again. 
- For this project, you’ll need to set the min and max number that your dice can produce. 
- For the average die, that means a minimum of 1 and a maximum of 6. 
- You’ll also want a function that randomly grabs a number within that range and prints it



Code Explaination: 

Because we need to generate random values that singnifying the randomness when you throw a die, we will import a module called 'random'.
This random module will let us do exactly that => Generate random values.

Next I defined a function naming roll_dice which will contain the essential code required for the dice to be rolled.
Inside the function I declare a variable which will save the value of rolled dice. 
For that we 'randint' property of 'random' module. To achieve that we could have also gone for some other random module properties such as random.random() or random.uniform(1, 10). 
But using random.random() will give us a random number between 0 & 1. And with random.uniform() although we can specify the range but the output would be a floating point number.
For rolling a die we needed a whole number or integer hence I went with random.randint().

After the function we declare a variable 'continu' and specify its value to be "Y". This variable will be used to prompt user and ask if they want to continue rolling the dice after they have already rolled it.

In the final section of our program we'll be using a while loop because we want this program to run until the user wants to exit. For that I provide the condition that this while loop will run till ' continu == "Y" '.

Inside the while loop I simply called the roll_dice function and then ask the user if they want to continue. If they want to then the loop will continue to call the function and roll the dice.
If they don't want to continue the if-else condition will check these and print a message saying "Thank You for Using" and then exit the program. 
