import random

def roll_dice():
	dice = random.randint(1, 6)
	print("The dice rolled successfully and value is : ", dice, sep=" ")


continu = "Y"
while continu == "Y":
		print("----------------------------------------------------")
		wait = input("Press any key to roll the dice :")
		roll_dice();
		continu = input("Do you want to roll dice [Y/N] : ")
		if continu != "Y":
			print("Thanks for using this program")
		print("----------------------------------------------------")

