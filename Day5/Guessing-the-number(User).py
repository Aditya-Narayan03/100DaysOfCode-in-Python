import random

low = 1
high = int(input("Enter the range : "))
hint = ''
while hint != "c":
    if high != low:
        comp_guess = random.randint(low, high)
    
    else:
        print("Stop messing with me...... I want to win")
    print(f"My guess is {comp_guess}.")
    hint = input("Is it Larger[L], Smaller[S] or Correct[C] : ").lower()
    if hint == "l":
        high = high - 1

    elif hint == "s":
        high = high + 1

print("YAY!!!!.....I got it right!!\nComputer always wins")